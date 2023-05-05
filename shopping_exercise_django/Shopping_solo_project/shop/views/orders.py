from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import *
from django.http import JsonResponse
import json 
import datetime
from urllib.error import HTTPError


def order_list(request):
    try:
        orders = Order.objects.all()
        return render(request, 'shop/order_list.html', {'orders' : orders})
    except:
        return redirect(request, 'shop/404.html')

def order_detail(request, id):
    try:
        order = get_object_or_404(Order, id=id)
        customer = order.customer
        user = get_object_or_404(User, id=customer.pk)
        line_items = LineItem.objects.filter(order_id=order.id)
        return render(request, 'shop/order_detail.html', {'order' : order, 'user': user, 'line_items': line_items})
    except:
        return redirect(request, 'shop/404.html')


def cartList(request):
    try:
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer = customer, complete=False)
            items = order.lineitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
            cartItems = order['get_cart_items']
            
        context = {'items':items, 'order':order, 'cartItems':cartItems}
        return render(request, 'shop/cart.html', context)
    except:
        return redirect(request, 'shop/404.html')


def checkout(request):
    try:
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer = customer, complete=False)
            items = order.lineitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
            cartItems = order['get_cart_items']
        context = {'items':items, 'order':order, 'cartItems': cartItems}
        return render(request, 'shop/checkout.html', context)
    except:
        return redirect(request, 'shop/404.html')


def updateItem(request):
    try:
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        product = Product.objects.get(id=productId)
        line_items, created =LineItem.objects.get_or_create(order=order, product=product)
        
        if action == 'add':
            line_items.quantity = (line_items.quantity + 1)
        elif action == 'remove':
            line_items.quantity = (line_items.quantity - 1)
        line_items.save()
        
        if line_items.quantity <= 0:
            line_items.delete()

        return JsonResponse('Item was added', safe=False)
    except:
        return redirect(request, 'shop/404.html')


def processOrder(request):
    try:
        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(request.body)
        
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            total = float(data['form']['total'])
            
            
        if total == float(order.get_cart_total):
            order.complete = True
        order.save()
        
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
        else:
            print('User is not logged in ...')
        return JsonResponse('Payment submitted..', safe=False)
    except:
        return redirect(request, 'shop/404.html')


  

