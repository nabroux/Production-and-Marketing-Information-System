from django import forms

from .models import Customer

class CustomerForm(forms.ModelForm):
    customer_name = forms.CharField(max_length=10)
    phone = forms.CharField(max_length=10)
    city = forms.CharField(max_length=10)
    
    class Meta:
        model = Customer
        fields = '__all__'
