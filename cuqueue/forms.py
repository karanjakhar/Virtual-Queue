from django import forms
from .models import details
from django.utils.safestring import mark_safe
class NameForm(forms.ModelForm):
    name=forms.CharField(label=mark_safe("<br/>Name"),max_length=30)
    uid = forms.CharField(label=mark_safe("<br/>UID"),max_length=30)
    mobile_no = forms.IntegerField(label=mark_safe("<br/>Mobile No."))
    email = forms.EmailField(label=mark_safe("<br/>Email ID"),max_length=30)

    class Meta:
        model= details

        fields=('name','uid','mobile_no','email',)

class staffform(forms.Form):
    username=forms.CharField(label=mark_safe("<br/>Username"),max_length=30)
    password=forms.CharField(widget=forms.PasswordInput(render_value=True))
