from django import forms

class SearchFrom(forms.Form):
    search_text = forms.CharField(max_length=100, label='نام کنسرت',required=False)
