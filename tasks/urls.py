from django.urls import path
from tasks.views import managers_dashboard, employee_dashboard, test, create_form, view_task, update_task, delete_task


urlpatterns = [
    path('manager-dashboard/', managers_dashboard, name = 'manager-dashboard'),
    path("user-dashboard/", employee_dashboard),
    path('test/', test),
    path('create-form/', create_form, name = 'create-form'),
    path('view-task/', view_task),
    path('update-task/<int:id>/', update_task, name='update-task'),
    path('delete-task/<int:id>/', delete_task, name = 'delete-task'),
    
]