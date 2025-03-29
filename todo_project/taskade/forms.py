from django import forms
from .models import TODOO

class TaskForm(forms.ModelForm):
    class Meta:
        model = TODOO
        fields = ['title', 'description', 'completed']
