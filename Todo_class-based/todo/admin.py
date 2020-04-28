from django.contrib import admin
from .models import TodoList
from django.contrib.auth.models import Group

class Customemk(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id','todos','complete','manager')
    list_display_links = ('id','todos')
    list_editable = ('complete',)
    search_fields = ('todos','datetime')

# Register your models here.
admin.site.register(TodoList,Customemk)