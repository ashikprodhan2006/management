from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm, TaskDetailModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from django.db.models import Q, Max, Min, Avg, Count
from django.contrib import messages

def managers_dashboard(request):
    # tasks = Task.objects.all()
    # type = request.GET.get('type')
    type = request.GET.get('type', 'all')
    # print(request.GET)
    # print(type)

    # tasks = Task.objects.select_related('details').prefetch_related('assigned_to').all()

    # """ getting task count """
    # total_task = tasks.count()
    # completed_task = Task.objects.filter(status = "COMPLETED").count()
    # in_progress_task = Task.objects.filter(status = "IN_PROGRESS").count()
    # pending_task = Task.objects.filter(status = "PENDING").count()

    # count = {
    #     "total_task":
    #     "completed_task":
    #     "in_progress_task":
    #     "pending_task":
    # }

    counts = Task.objects.aaggregate(
        total = Count('id'),
        completed = Count('id', filter = Q(status = 'COMPLETED')),
        in_progress = Count('id', filter = Q(status = 'IN_PROGRESS')),
        pending = Count('id', filter = Q(status = 'PENDING'))
    )

    base_query = Task.objects.select_related('details').prefetch_related('assigned_to').all()
    
    if type == 'completed':
        tasks = base_query.filter(status = 'COMPLETED')
    elif type == 'in_progress':
        tasks = base_query.filter(status = 'IN_PROGRESS')
    elif type == 'pending':
        tasks = base_query.filter(status = 'PENDING')
    elif type == 'all':
        tasks = base_query.all()


    # context = {
    #     "tasks": tasks,
    #     "total_task": total_task,
    #     "completed_task": completed_task,
    #     "pending_task": pending_task,
    #     "in_progress_task": in_progress_task

    # }
    
    context = {
        "tasks": tasks,
        "counts": counts
    }
    
    return render(request, "dashboard/manager_dashboard.html", context);

def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html");


def test(request):
    context = {
        "names":['rakib', 'khan', 'sakib', 'raton', 'tamim khan'],
        "age":33
    }
    return render(request, "test.html", context);


def create_form(request):
    # employees = Employee.objects.all()
    # form = TaskForm(employees = employees)

    # form = TaskModelForm()

    task_form = TaskModelForm()
    task_detail_form = TaskDetailModelForm()

    if request.method == "POST":
        # form = TaskForm(request.POST, employees = employees)
        # form = TaskForm(request.POST)

        # form = TaskModelForm(request.POST)

        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST)

        if task_form.is_valid() and task_detail_form:
            """ For Model Form Data """
            task = task_form.save()
            task_detail = task_detail_form.save(commit = False)
            task_detail.task = task
            task_detail.save()

            # return render(request, 'dashboard/task_form.html', {"form": form, "message": "task added successfully"})

            messages.success(request, "Task Created Successfully")
            return redirect('create-task')

            # ''' For Django Form Data '''
            # print(form.cleaned_data)
            # data = form.cleaned_data
            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to')

            # task = Task.objects.create(
            #     title = title, description = description, due_date = due_date
            # )

            # # Assign employee to tasks
            # for emp_id in assigned_to:
            #     employee = Employee.objects.get(id = emp_id)
            #     task.assigned_to.add(employee)
            
            # return HttpResponse("Task Added successfully")
            

    # context = {
    #     "form": form
    # }

    context = {"task_form": task_form, "task_detail_form": task_detail_form}
    return render(request, "dashboard/task_form.html", context)


def update_task(request, id):
    # employees = Employee.objects.all()
    # form = TaskForm(employees = employees)

    # form = TaskModelForm()
    task = Task.objects.get(id = id)

    # task_form = TaskModelForm()
    # task_detail_form = TaskDetailModelForm()
    task_form = TaskModelForm(instance = task)
    if task.details:
        task_detail_form = TaskDetailModelForm(instance = task.details)

    if request.method == "POST":
        task_form = TaskModelForm(request.POST, instance = task)
        task_detail_form = TaskDetailModelForm(request.POST, instance = task.details)

        if task_form.is_valid() and task_detail_form:
            """ For Model Form Data """
            task = task_form.save()
            task_detail = task_detail_form.save(commit = False)
            task_detail.task = task
            task_detail.save()

           
            messages.success(request, "Task Updated Successfully")
            return redirect('update-task', id)


    context = {"task_form": task_form, "task_detail_form": task_detail_form}
    return render(request, "dashboard/task_form.html", context)


def delete_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id = id)
        task.delete()

        messages.success(request, 'Task Deleted Successfully')
        return redirect('manager-dashboard')
    else:
        messages.error(request, 'Somnthing went wrong')
        return redirect('manager-dashboard')

# def view_task(request):
    # select_related (ForeignKey, OneToOneField)

    # tasks = Task.objects.all()
    # tasks = Task.objects.select_related('details').all()
    # tasks = TaskDetail.objects.select_related('task').all()
    # tasks = Task.objects.select_related('project').all()
    # tasks = Project.objects.select_related('task_set').all()

    """ prefetch_related (reverse ForeignKey, ManyToMany) """
    # tasks = Project.objects.prefetch_related('task_set').all()
    # tasks = Project.objects.all()
    # tasks = Task.objects.prefetch_related('assigned_to').all()

    # return render(request, "show_task.html", {"tasks": tasks})


def view_task(request):
    # task_count = Task.objects.aggregate(num_task = Count('id'))
    # task_count = Project.objects.annotate(num_task = Count('task'))
    projects = Project.objects.annotate(num_task = Count('task')).order_by('num_task')

    return render(request, "show_task.html", {"projects": projects})