from django import forms
class ContastantRegstration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    cf_handle = forms.CharField()