from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class ProfileFrom(forms.ModelForm):
    class Meta:
        model = users
        fields = ['username', 'first_name', 'last_name', 'email',
                  'user_phone', 'user_photo']


class RegStaff(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'input'}))
    user_phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'input'}))

    class Meta:
        model = users
        fields = ['username', 'first_name', 'last_name', 'email', 'user_phone',
                  'password1', 'password2', 'user_note', 'user_role', ]


class Login(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input'}))


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = users
        fields = ['username', 'first_name', 'last_name', 'email',
                  'user_phone', 'user_photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class AddTaskFrom(forms.ModelForm):
    class Meta:
        model = tasks
        fields = "__all__"


class AddOrdersFrom(forms.ModelForm):
    class Meta:
        model = orders
        fields = "__all__"


class AddInventFrom(forms.ModelForm):
    class Meta:
        model = inventory
        fields = "__all__"


class AddSalesFrom(forms.ModelForm):
    class Meta:
        model = sales
        fields = "__all__"


class AddClientFrom(forms.ModelForm):
    class Meta:
        model = client
        fields = "__all__"
