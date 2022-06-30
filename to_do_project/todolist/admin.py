from django.contrib import admin

# Register your models here.
from .models import Todolist
@admin.register(Todolist)
class Useradmin(admin.ModelAdmin):
    list_display=('id','name')