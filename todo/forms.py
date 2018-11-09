from django import forms


class TodoForm(forms.Form):
    item = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
