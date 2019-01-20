from django import forms

from CRM.models import Order,Product,Customer

    
class OrderForm(forms.ModelForm):  
    order_No = forms.IntegerField()
    created_time = forms.DateField()
    product = forms.ModelChoiceField(queryset = Product.objects.all(), empty_label="請選擇")
    quantity = forms.IntegerField()  
    customer_name = forms.ModelChoiceField(queryset=Customer.objects.all(), empty_label="請選擇")
    
    class Meta:
        model = Order
        fields = '__all__'
