from django.shortcuts import render
from django.http import HttpResponse

# def managers_dashboard(request):
#     return render(request, "dashboard/u_d.html");
    

# def managers_dashboard(request):
#     return render(request, "dashboard_project.html");
#     # return render(request, "dashboard.html");

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the task menagement system");

def contact(request):
    return HttpResponse("This is contact page");

def contact(request):
    return HttpResponse("<h1 style = 'color: red'>This is contact page</h1>");

def show_task(request):
    return HttpResponse("This is show tasks");

def show_specific_task(request, id):
    print("id", id);
    print("id type:", type(id));
    return HttpResponse(f"This is specific task page: {id}");


 
