from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task

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
 
