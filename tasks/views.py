# tasks/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm

# -----------------------------
# Class-Based View → List tasks
# -----------------------------
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"
    login_url = "login"  # redirect to login page if not logged in

    def get_queryset(self):
        # Only show incomplete tasks for the logged-in user
        return Task.objects.filter(user=self.request.user, completed=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add completed tasks to context for optional separate display
        context['completed_tasks'] = Task.objects.filter(user=self.request.user, completed=True)
        return context

# -----------------------------
# Class-Based View → Add task
# -----------------------------
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/add_task.html"
    success_url = reverse_lazy("todo:task-list")
    login_url = "login"  # redirect to login page if not logged in

    def form_valid(self, form):
        # Assign the current user to the new task
        form.instance.user = self.request.user
        return super().form_valid(form)

# -----------------------------
# Function-Based View → Toggle task completion
# -----------------------------
def toggle_task(request, pk):
    if not request.user.is_authenticated:
        return redirect("login")
    # Ensure task belongs to logged-in user
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect("todo:task-list")

# -----------------------------
# Function-Based View → Delete task (optional)
# -----------------------------
def delete_task(request, pk):
    if not request.user.is_authenticated:
        return redirect("login")
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect("todo:task-list")

# -----------------------------
# Function-Based View → Register new user
# -----------------------------
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # after registration → login page
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

# -----------------------------
# Function-Based View → Logout user
# -----------------------------
def logout_view(request):
    logout(request)  # ends the user session
    return redirect("login")
