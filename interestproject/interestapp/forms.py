from django import forms


class formname(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()
    principal = forms.FloatField()
    interest = forms.IntegerField(required=False)
