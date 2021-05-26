import datetime
import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)

from . models import Rent, Order, OrderItem
from  users.models import Profile
# from .utils import cartData, cookieCart, guestOrder

from django.shortcuts import render
from django.http import JsonResponse

class RentListView(ListView):
    model = Rent
    template_name = 'rent/list.html'
    context_object_name = 'rent'
    ordering = ['-title']
    paginate_by = 4


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        order = {'get_cart_total':0, 'get_cart_items':0}
        items = []

    context = {'items':items, 'order':order}
    return render(request, 'rent/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        order = {'get_cart_total':0, 'get_cart_items':0}
        items = []

    context = {'items':items, 'order':order}
    return render(request, 'rent/checkout.html', context)  

def updateItem(request):
    #data = json.loads(request.data)
    #productId = data['productId']
    #action = data['action']

    #print(productId, action)
    return JsonResponse('Item was added', safe=False)  
