from django.urls import path
from .import views



urlpatterns = [
    path('',views.Index.as_view(), name = 'home'),
    path('AddTodo/',views.AddTodo.as_view(), name = 'add'),
    path('Todoupdate/<int:pk>',views.Todoupdate.as_view(), name = 'update'),
    path('Deletetodo/<int:pk>',views.Deletetodo.as_view(), name = 'delete'),
    path('Signup/',views.Signup.as_view(), name = 'signup'),
]