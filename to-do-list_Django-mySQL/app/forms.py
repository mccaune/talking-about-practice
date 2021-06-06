from django import forms
from .models import Tasks

    
class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['task_id', 'title', 'description']
        labels = {
            'title': 'Task title', 
            'description': 'Task description',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows':4})
        }
