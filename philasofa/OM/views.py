from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse

from .forms import OrderForm
from CRM.models import Customer,Order,Product
from .module import *
# Create your views here.

#作管首頁
def om_index(request):
    return render(request,'om_index.html',{
    
    })
    
    
def add_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            p = order.product
            order_q = order.quantity
            costInventory(p,order_q)

            return redirect('om_index')
    else:
        form = OrderForm()        

    form = OrderForm()
    return render(request, 'forms/add_order.html', {'form': form})


def view_order(request):
    orders = Order.objects.order_by('-order_No')
    context = {'orders':orders} 
    
    return render(request, 'view_order.html', context)

def search_order(request):
    if 'o_no' in request.GET:
        order_no = request.GET['o_no']
        res = returnOrders_by_No(order_no)
    else:
        res = 'none'

    return render_to_response('search_order.html', {'res':res} )


def view_product(request):
    products = Product.objects.all()
    ROP_string = create_ROP_string()
    EOQ_string = create_EOQ_string()
    demand_string = create_monthlyDemandList_string()

    context = {'products':products,'ROP_string':ROP_string,'EOQ_string':EOQ_string,'demand_string':demand_string}
    return render(request, 'view_product.html', context)


#Other
def costInventory(p,order_q):
    p.inventory_quantity -= order_q
    p.save()

