from django import forms
from .models import *


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
