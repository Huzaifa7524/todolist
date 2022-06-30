from django import forms
from .models import Todolist

class Todo(forms.ModelForm):
    class Meta:
        model=Todolist
        fields=['name']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'})
        }