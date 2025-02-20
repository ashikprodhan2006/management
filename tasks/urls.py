
from django.urls import path
from tasks.views import manager_dashboard, employee_dashboard, view_task, update_task, delete_task, event_management, dashboard, event, event_form


urlpatterns = [
    path('manager-dashboard/', manager_dashboard, name = 'manager-dashboard'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path("user-dashboard/", employee_dashboard, name='user-dashboard'),
    path('view-task/', view_task),
    path('update-task/<int:id>/', update_task, name='update-task'),
    path('delete-task/<int:id>/', delete_task, name = 'delete-task'),
    path('event-management/', event_management, name = 'event-management'),
    path('event/', event, name = 'event'),
    path('event-form/', event_form, name = 'event-form'),
    
]