from django.urls import path
from tasks.views import manager_dashboard, employee_dashboard, create_task, view_task, update_task, delete_task, event_management, dashboards, event, event_form, task_details


urlpatterns = [
    path('manager-dashboard/', manager_dashboard, name = 'manager-dashboard'),
    path('dashboard/', dashboards, name = 'dashboard'),
    path("user-dashboard/", employee_dashboard, name='user-dashboard'),
    path('create-task/', create_task, name='create-task'),
    path('view-task/', view_task),
    path('update-task/<int:id>/', update_task, name='update-task'),
    path('delete-task/<int:id>/', delete_task, name = 'delete-task'),
    path('event-management/', event_management, name = 'event-management'),
    path('event/', event, name = 'event'),
    path('event-form/', event_form, name = 'event-form'),
    path('task/<int:task_id>/details/', task_details, name='task-details'),
    
]



