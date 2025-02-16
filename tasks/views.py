from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm, TaskDetailModelForm, EventForm
from tasks.models import Employee, Task, TaskDetail, Project, Event
from django.db.models import Q, Max, Min, Avg, Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required


# Create your views here.
def is_manager(user):
    return user.groups.filter(name='Manager').exists()

def is_employee(user):
    return user.groups.filter(name='Manager').exists()

@user_passes_test(is_manager, login_url='no-permission')
def managers_dashboard(request):
    type = request.GET.get('type', 'all')
   

    counts = Task.objects.aggregate(
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


    context = {
        "tasks": tasks,
        "counts": counts,
    }
    
    return render(request, "dashboard/manager_dashboard.html", context);



def dashboard(request):
    return render(request, "dashboard/dashboard.html");

@user_passes_test(is_employee)
def employee_dashboard(request):
    return render(request, "dashboard/user_dashboard.html");


def test(request):
    context = {
        "names":['rakib', 'khan', 'sakib', 'raton', 'tamim khan'],
        "age":33
    }
    return render(request, "test.html", context);


@login_required
@permission_required("tasks.add_task", login_url='no-permission')
def create_form(request):
    task_form = TaskModelForm()
    task_detail_form = TaskDetailModelForm()

    if request.method == "POST":

        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST)

        if task_form.is_valid() and task_detail_form:
            """ For Model Form Data """
            task = task_form.save()
            task_detail = task_detail_form.save(commit = False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, "Task Created Successfully")
            return redirect('create-form')

       
    context = {"task_form": task_form, "task_detail_form": task_detail_form}
    return render(request, "dashboard/task_form.html", context)




# def update_task(request, id):
#     task = Task.objects.get(id = id)
#     task_form = TaskModelForm(instance = task)
#     if task.details:
#         task_detail_form = TaskDetailModelForm(instance = task.details)

#     if request.method == "POST":
#         task_form = TaskModelForm(request.POST, instance = task)
#         task_detail_form = TaskDetailModelForm(request.POST, instance = task.details)

#         if task_form.is_valid() and task_detail_form:
#             """ For Model Form Data """
#             task = task_form.save()
#             task_detail = task_detail_form.save(commit = False)
#             task_detail.task = task
#             task_detail.save()

           
#             messages.success(request, "Task Updated Successfully")
#             return redirect('update-task', id)


#     context = {"task_form": task_form, "task_detail_form": task_detail_form}
#     return render(request, "dashboard/task_form.html", context)

@login_required
@permission_required("tasks.update_task", login_url='no-permission')
def update_task(request, id):
    task = Task.objects.get(id=id)
    task_form = TaskModelForm(instance=task)

    # Check if task.details exists
    task_detail_form = TaskDetailModelForm(instance=task.details) if hasattr(task, 'details') else TaskDetailModelForm()

    if request.method == "POST":
        task_form = TaskModelForm(request.POST, instance=task)
        task_detail_form = TaskDetailModelForm(request.POST, instance=task.details if hasattr(task, 'details') else None)

        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, "Task Updated Successfully")
            return redirect('update-task', id)

    context = {"task_form": task_form, "task_detail_form": task_detail_form}
    return render(request, "dashboard/task_form.html", context)


@login_required
@permission_required("tasks.delete_task", login_url='no-permission')
def delete_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id = id)
        task.delete()

        messages.success(request, 'Task Deleted Successfully')
        return redirect('manager-dashboard')
    else:
        messages.error(request, 'Something went wrong')
        return redirect('manager-dashboard')

@login_required
@permission_required("tasks.view_task", login_url='no-permission')
def view_task(request):
    projects = Project.objects.annotate(num_task=Count('tasks')).order_by('num_task')

    return render(request, "show_task.html", {"projects": projects})





def event_management(request):
    return render(request, "event_management.html")

def event_management1(request):
    return render(request, "event_management1.html")

def event_form(request):
    return render(request, "event_form.html")

def event(request):
    return render(request, "event.html")




# /////////////////////////////////////////


def event(request):
    events = Event.objects.all()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm()

    return render(request, "index.html", {"form": form, "events": events})
