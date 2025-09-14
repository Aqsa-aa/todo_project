

from django.urls import path
from .views import TaskListView, TaskCreateView, toggle_task, register
from . import views   # make sure this line exists
app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("add/", TaskCreateView.as_view(), name="task-create"),
    path("toggle/<int:pk>/", toggle_task, name="task-toggle"),
     path("delete/<int:pk>/", views.delete_task, name="task-delete"),  # optional
    path("register/", register, name="register"),
    path('logout/', views.logout_view, name='logout'),
]

