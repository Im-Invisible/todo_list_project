from re import T
from statistics import mode
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Task


class customLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_auhenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class taskList(ListView):
    model = Task
    context_object_name = 'tasks'


class taskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class taskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class taskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class taskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

