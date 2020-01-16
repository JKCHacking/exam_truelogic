from django import forms
from JKC_numbering_system.models import Current_User

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=200)

    class Meta:
        model = Current_User
        fields =['username', 'password',]