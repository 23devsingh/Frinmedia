from django import forms
from django.contrib.auth.models import User

class SearchForm(forms.Form):
    query = forms.CharField()