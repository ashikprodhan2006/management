from django.urls import path
from tasks.views import manager_dashboard, employee_dashboard, create_task, view_task, update_task, delete_task, task_details, dashboard, event_management, event, event_form, Greetings, HiGreetings, HiHowGreetings, CreateTask, ViewProject, TaskDetail, UpdateTask, ManagerDashboardView, EmployeeDashboardView, DeleteTaskView, EventManagementView

urlpatterns = [
    # path('manager-dashboard/', manager_dashboard, name="manager-dashboard"),
    path('manager-dashboard/', ManagerDashboardView.as_view(), name="manager-dashboard"),
    # path('user-dashboard/', employee_dashboard, name='user-dashboard'),
    path('user-dashboard/', EmployeeDashboardView.as_view(), name='user-dashboard'),
    # path('create-task/', create_task, name='create-task'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    # path('view-task/', view_task, name='view-task'),
    path('view-task/', ViewProject.as_view(), name='view-task'),
    # path('task/<int:task_id>/details/', task_details, name='task-details'),
    path('task/<int:task_id>/details/', TaskDetail.as_view(), name='task-details'),
    # path('update-task/<int:id>/', update_task, name='update-task'),
    path('update-task/<int:id>/', UpdateTask.as_view(), name='update-task'),
    # path('delete-task/<int:id>/', delete_task, name='delete-task'),
    path('delete-task/<int:id>/', DeleteTaskView.as_view(), name='delete-task'),
    path('dashboard/', dashboard, name='dashboard'),

    # path('event-management/', event_management, name = 'event-management'),
    path('event-management/', EventManagementView.as_view(), name = 'event-management'),
    path('event/', event, name = 'event'),
    path('event-form/', event_form, name = 'event-form'),

    path('greetings/', Greetings.as_view(), name='greetings'),
    path('higreetings/', HiGreetings.as_view(), name='higreetings'),
    path('hihowgreetings/', HiHowGreetings.as_view(greetings='Hi Good Day'), name='hihowgreetings'),
]