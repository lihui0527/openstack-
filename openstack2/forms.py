from django import forms
 
class AddForm(forms.Form):
    username = forms.IntegerField()
    password = forms.IntegerField()
