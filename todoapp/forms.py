
from django import forms
from .models import Todo
from dataclasses import fields

class TodoForm(forms.ModelForm):
    class Meta():
        model = Todo
        fields = ["first_name","Location",'branche']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'item','placeholder' : 'Add Item'}),
        }