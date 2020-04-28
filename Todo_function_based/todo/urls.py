from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('addtodo/',views.addtodo, name='add'),
    path('todo/complete/<int:id>/',views.todocomplete, name='done'),
    path('todoupdate/<int:id>/',views.todoupdate, name='update'),
    path('deleteCom/',views.deleteCom, name='deletecomplete'),
    path('deleteAll/',views.deleteAll, name='deleteall'),
]