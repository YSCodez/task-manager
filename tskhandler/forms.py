from django import forms
from .models import TaskAllocA

class TaskAllocForm(forms.ModelForm):
    class Meta:
        model = TaskAllocA
        fields = ['task']
        widgets = {
            'task': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
