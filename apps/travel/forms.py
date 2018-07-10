import re
from django import forms
from .models import Order
from .models import Scenic
class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['otime','omemnum','sname','oname','ophone','oremark','totalprice']


