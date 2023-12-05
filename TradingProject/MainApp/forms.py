from django import forms
from  .models import treadingfile

class tradingform(forms.Form):
    file=forms.FileField()
    upload_time = forms.DateTimeField()