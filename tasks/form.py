from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    # Meta is used to provide more infor to django and tell django how to deal with data and form
    class Meta:
        model = Task
        fields = ["content", "due_date"]
        # widget is used to define feature of input
        widget = {
            "content" : forms.TextInput(attrs={"placeholder": "Enter your task..."}),
            "due_date" : forms.DateTimeInput(attrs={"type" : "datetime-local"})  # date selecter
        }