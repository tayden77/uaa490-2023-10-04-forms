from django import forms
from .models import Task

class TaskNameForm(forms.Form):
    task = forms.CharField(label="Task to delete")

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
