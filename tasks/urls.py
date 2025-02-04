from django.urls import path
from tasks.views import managers_dashboard, user_dashboard, test, create_form, view_task
# from tasks.views import test
# from tasks.views import create_forms, view_task, update_task, delete_task





# urlpatterns = [
#     # path('show-task/', show_task),
#     # path('view-task/', view_task),
#     # path('test/', test),
#     # path('create-forms/', create_forms, name = 'create-forms'),
#     # path('pydate-task/<int:id>/', update_task, name = 'update-task'),
#     # path('delete-task/<int:id>/', delete_task, name = 'delete-task')

# ]
urlpatterns = [
    path('manager-dashboard/', managers_dashboard),
    path("user-dashboard/", user_dashboard),
    path('test/', test),
    path('create-form/', create_form),
    path('view-task/', view_task),
]