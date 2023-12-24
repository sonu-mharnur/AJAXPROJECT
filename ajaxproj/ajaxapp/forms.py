from django import forms

class uploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    filename = forms.FileField()