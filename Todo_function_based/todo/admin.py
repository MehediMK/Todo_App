from django.contrib import admin
from .models import TodoModel

class TodoAdminCustome(admin.ModelAdmin):
    list_display = ('id','todos','complete',)
    list_editable = ('complete',)
    list_display_links = ('id','todos',)


# Register your models here.
admin.site.register(TodoModel,TodoAdminCustome)