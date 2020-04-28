from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TodoList(models.Model):
    manager = models.ForeignKey(User,on_delete=models.CASCADE,default = None)
    todos = models.CharField(max_length=30,blank=False)
    complete = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.todos
