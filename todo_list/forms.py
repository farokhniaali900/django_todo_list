from django import forms
from .models import todo_objects

class TodoForm(forms.ModelForm):
    class Meta:
        model = todo_objects
        fields = [
            'title',
            'task',
        ]