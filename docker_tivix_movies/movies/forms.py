from django import forms
import datetime
from django.core.exceptions import ValidationError

def year_validator(value):
    if value < 1896 or value > datetime.datetime.now().year:
        raise ValidationError("Enter a valid year")

class MovieSearchForm(forms.Form):
    title = forms.CharField(label="Title ", max_length=200)
    year = forms.IntegerField(label="Year ",validators=[year_validator],required=False)
