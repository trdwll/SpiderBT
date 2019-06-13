from django.urls import path, include

from SpiderBT_Scrum.views import IndexTaskView, CreateTaskView#, UpdateTaskView, DeleteTaskView

urlpatterns = [
    path('<slug>/tasks/', IndexTaskView.as_view(), name='index_tasks'),
    path('<slug>/tasks/create/', CreateTaskView.as_view(), name='create_task'),
    #path('<slug>/tasks/update/<id>/', UpdateTaskView.as_view(), name='update_task'),
    #path('<slug>/tasks/delete/<id>/', DeleteTaskView.as_view(), name='delete_task'),
]