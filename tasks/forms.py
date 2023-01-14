from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control ', 'placeholder' : 'Write a title for the Task'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder' : 'Write your description for youy task'}),
            'important': forms.CheckboxInput(attrs={
                'class': 'form-check-input translete-middle'}),
        }
