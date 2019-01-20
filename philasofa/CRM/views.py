from django.shortcuts import render,redirect, render_to_response
from django.http import HttpResponse

from .forms import CustomerForm
from .models import Customer,Order,Product
from .module import *

# Create your views here.

#顧管首頁
def home(request):
    return render(request,'home.html',{
    
    })

def crm_index(request):
    return render(request,'crm_index.html',{
    
    })
    
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('crm_index')
    else:
        form = CustomerForm()        

    form = CustomerForm()
    return render(request, 'forms/add_customer.html', {'form': form})
    
def view_customer(request):
    customers = Customer.objects.all()
    retentionrate2017 = calculate_retentionrate(2017)
    retentionrate2018 = calculate_retentionrate(2018)
    surviverate2017 = calculate_surviverate(2017)
    surviverate2018 = calculate_surviverate(2018)

    city_string = create_city_string()

    context = {'customers':customers,'r17':retentionrate2017,'r18':retentionrate2018,'s17':surviverate2017,'s18':surviverate2018,'city_string':city_string}
    
    return render(request, 'view_customer.html', context)

def search_customer(request):
    if 'c_name' in request.GET:
        customer_n = request.GET['c_name']
        customer_id = returnID_by_CustomerName(customer_n)
        customer_monetary = getMonetary_by_ID(customer_id)
        customer_RFM = getRFM_by_ID(customer_id)

        customer_orders = returnOrders_by_CustomerName(customer_n)

        res = Customer.objects.filter(customer_name = customer_n)
    else:
        customer_orders = []
        customer_monetary = 0
        customer_RFM = 0
        res = 'none'

    return render_to_response('search_customer.html', {'res':res,'monetary':customer_monetary,'RFM':customer_RFM,'customer_orders':customer_orders} )

# other function
def createCustomerDict():
    res = {}
    customers = Customer.objects.all()
    for customer in customers:
        id = customer.id
        res[id] = {'name':customer.customer_name,'phone':customer.phone,'city':customer.city,'monetary':getMonetary_by_ID(id),'RFM':getRFM_by_ID(id)}
    return res

def createMonetaryList():
    res = []
    customers = Customer.objects.all()
    for customer in customers:
        id = customer.id
        monetary = getMonetary_by_ID(id)
        res.append(monetary)
    return res

def createRFMList():
    res = []
    customers = Customer.objects.all()
    for customer in customers:
        id = customer.id
        RFM = getRFM_by_ID(id)
        res.append(RFM)
    return res
