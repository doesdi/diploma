from django import forms
from .models import *


class ProfileFrom(forms.ModelForm):
    class Meta:
        model = users
        fields = ['username', 'first_name', 'last_name', 'email',
                  'user_phone', 'user_note', 'user_time', 'last_login', 'user_photo']



class ProfileUpdateForm(forms.ModelForm):
    """
    Форма обновления данных профиля пользователя
    """
    class Meta:
        model = users
        fields = ['username', 'first_name', 'last_name', 'email',
                  'user_phone', 'user_note', 'user_time', 'last_login', 'user_photo']

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы обновления
        """
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
