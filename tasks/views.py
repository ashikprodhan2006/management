from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from django.db.models import Q, Max, Min, Avg, Count

def managers_dashboard(request):
    return render(request, "dashboard/manager_dashboard.html");
    

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

    form = TaskModelForm()

    if request.method == "POST":
        # form = TaskForm(request.POST, employees = employees)
        # form = TaskForm(request.POST)

        form = TaskModelForm(request.POST)

        # task_form = TaskModelForm(request.POST)
        # task_detail_form = TaskDetailModelForm(request.POST)

        if form.is_valid():
            """ For Model Form Data """
            print(form)
            form.save()

            return render(request, 'dashboard/task_form.html', {"form": form, "message": "task added successfully"})

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
            

    context = {
        "form": form
    }
    return render(request, "dashboard/task_form.html", context)
 

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