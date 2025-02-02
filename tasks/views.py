from django.shortcuts import render
from django.http import HttpResponse

def managers_dashboard(request):
    return render(request, "dashboard/manager_dashboard.html");
    

def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html");


def test(request):
    return render(request, 'test.html')



 
