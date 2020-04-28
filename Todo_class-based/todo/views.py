from django.shortcuts import render,redirect
from .models import TodoList
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class Index(LoginRequiredMixin,ListView):
    template_name = 'index.html'
    model = TodoList
    context_object_name = 'todo'
    def get_queryset(self):
        todo = super().get_queryset()
        return todo.filter( manager = self.request.user )

class AddTodo(LoginRequiredMixin,CreateView):
    template_name = 'AddTodo.html'
    model = TodoList
    fields = ['todos','complete']
    # success_url = '/'
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.manager=self.request.user
        instance.save()
        return redirect('home')

class Todoupdate(LoginRequiredMixin,UpdateView):
    template_name = 'Todoupdate.html'
    model = TodoList
    fields = ['todos','complete']
    context_object_name = 'todo'
    # success_url = '/'
    def form_valid(self,form):
        instance = form.save(commit=False)
        if instance.manager == self.request.user:
            instance.save()
            return redirect('/')
        else:
            return redirect('/')

class Deletetodo(LoginRequiredMixin,DeleteView):
    template_name = 'Deletetodo.html'
    model = TodoList
    context_object_name = 'todo'
    success_url = '/'

class Signup(CreateView):
    template_name = 'registration/Signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    