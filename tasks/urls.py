from django.urls import path
from tasks.views import managers_dashboard, user_dashboard, test, create_form, view_task, update_task, delete_task, event_management, dashboard, event, event_form, event


urlpatterns = [
    path('manager-dashboard/', managers_dashboard, name = 'manager-dashboard'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path("user-dashboard/", user_dashboard),
    path('test/', test),
    path('create-form/', create_form, name = 'create-form'),
    path('view-task/', view_task),
    path('update-task/<int:id>/', update_task, name='update-task'),
    path('delete-task/<int:id>/', delete_task, name = 'delete-task'),
    path('event-management/', event_management, name = 'event-management'),
    path('event/', event, name = 'event'),
    path('event-form/', event_form, name = 'event-form'),
    
]