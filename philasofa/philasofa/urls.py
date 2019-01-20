"""philasofa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from CRM.views import home,crm_index,add_customer,view_customer,search_customer
from OM.views import om_index,add_order,search_order,view_order,view_product


urlpatterns = [
    url(r'^$',home),
    url(r'^admin/', include(admin.site.urls)),
    
    #CRM
    url(r'^crm_index/$', crm_index, name='crm_index'),
    url(r'^crm_index/add_customer/$', add_customer, name='add_customer'),
    url(r'^crm_index/view_customer/$',view_customer, name='view_customer'),
    url(r'^crm_index/search_customer/$',search_customer, name='search_customer'),
    
    #OM
    url(r'^om_index/$', om_index, name = 'om_index'),
    url(r'^om_index/add_order/$', add_order, name='add_order'),
    url(r'^om_index/search_order/$', search_order, name='search_order'),
    url(r'^om_index/view_order/$', view_order, name='view_order'),
    url(r'^om_index/view_product/$', view_product, name='view_product'),
]
