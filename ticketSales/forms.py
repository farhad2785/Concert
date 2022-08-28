from django import forms
from . import models



class SearchFrom(forms.Form):
    search_text = forms.CharField(max_length=100, label='نام کنسرت',required=False)


class ConcerForm(forms.ModelForm):
    class Meta:
        model = models.ConcertModel
        fields = ['name','singer_name','lenght','poster']
        # exclude = ['poster']