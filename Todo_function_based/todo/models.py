from django.db import models

# Create your models here.
class TodoModel(models.Model):
    todos = models.CharField(max_length=20,blank=False)
    complete = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(salf):
        return salf.todos

    class Meta:
        ordering = ['-id']
