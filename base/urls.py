from django.urls import path
from .views import  taskList, taskDetail, taskCreate, taskUpdate, taskDelete

urlpatterns = [
    path('', taskList.as_view(), name='tasks'),
    path('task/<int:pk>/', taskDetail.as_view(), name='task'),
    path('task-create/', taskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', taskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', taskDelete.as_view(), name='task-delete'),
]
