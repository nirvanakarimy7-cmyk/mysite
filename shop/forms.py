from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django import forms
from .models import Profile


class updateuserInfo(forms.ModelForm):
    phone=forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'phone number :'}),
        required=False)
    address1=forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'your first address :'}),
        required=False)
    address2=forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'your second address :'}),
        required=False)
    city=forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'city:'}),
        required=False)
    state=forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'state :'}),
        required=False)
    zipcode=forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'zipcode :'}),
        required=False)
    countary=forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'countary :'}),
        required=False)

    class Meta:
        model=Profile
        fields=('phone','address1','address2','state','zipcode','countary')


class updatepass(SetPasswordForm):
    new_password1=forms.CharField(
    label="",
    widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'name':'password',
            'type':'password',
            'placeholder':'enter your password (more than 8 charactor )'
        }
    )

    )
    new_password2=forms.CharField(
    label="",
    widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'name':'password',
            'type':'password',
            'placeholder':'enter your password again'
        }
    )
    )
    class Meta:
        model=User
        fields=['new_password1','new_password2']

class updateuserform(UserChangeForm):
    password=None
    first_name= forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'enter your name'})
        ,required=False
    )
    last_name= forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'enter your last name'})
        ,required=False
    )
    email= forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'enter your email'})
        ,required=False
    )
    username = forms.CharField(
    label="",
    max_length=20,
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'enter your user name'
        }
    )
    ,required=False
)
    password1=forms.CharField(
    label="",
    widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'name':'password',
            'type':'password',
            'placeholder':'enter your password (more than 8 charactor )'
        }
    )

    )

    class Meta:
        model=User
        fields = [
    'first_name',
    'last_name',
    'email',
    'username',
]


class signupform(UserCreationForm):
    first_name= forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'enter your name'})
    )
    last_name= forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'enter your last name'})
    )
    email= forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'enter your email'})
    )
    username = forms.CharField(
    label="",
    max_length=20,
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'enter your user name'
        }
    )
)
    password1=forms.CharField(
    label="",
    widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'name':'password',
            'type':'password',
            'placeholder':'enter your password (more than 8 charactor )'
        }
    )

    )
    password2=forms.CharField(
    label="",
    widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'name':'password',
            'type':'password',
            'placeholder':'enter your password again'
        }
    )
    )
    class Meta:
        model=User
        fields = [
    'first_name',
    'last_name',
    'email',
    'username',
    'password1',
    'password2'
]