from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class':'list-group-item',
                'name':'todoitem',
                'placeholder':'Enter your Todo',
            }
        ),
        label=''
    )