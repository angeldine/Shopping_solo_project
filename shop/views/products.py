from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from shop.forms import BasketAddProductForm, ProductForm
from shop.models import *
import json
from django.http import JsonResponse
from urllib.error import HTTPError

def product_list(request):
    try:
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.lineitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
            cartItems = order['get_cart_items']
        products = Product.objects.all()
        context = {'products': products, 'cartItems':cartItems}    
        return render(request, 'shop/product_list.html', context)
    except HTTPError as err:
        if err.code == 404:
            return render(request, 'shop/404.html')
        if err.code == 400:
            return render(request, 'shop/404.html')
        if err.code == 500:
            return render(request, 'shop/500.html',)
        else:
            raise



def product_detail(request, id):
    try:
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer,complete=False)
            items = order.lineitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
            cartItems = order['get_cart_items']
        product = get_object_or_404(Product, id=id)
        basket_product_form = BasketAddProductForm()
        context = {'product' : product, 'basket_product_form': basket_product_form, 'cartItems':cartItems }
        return render(request, 'shop/product_detail.html', context )
    except:
        return render(request, 'shop/404.html')

def product_new(request):
    try:
        if request.method=="POST":
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.created_date = timezone.now()
                product.save()
                return redirect('shop:product_detail', id=product.id)
        else:
            form = ProductForm()
        return render(request, 'shop/product_edit.html', {'form': form})
    except HTTPError as err:
        if err.code == 404:
            return render(request, 'shop/404.html')
        if err.code == 400:
            return render(request, 'shop/404.html')
        if err.code == 500:
            return render(request, 'shop/500.html',)
        else:
            raise


def product_edit(request, id):
    try:
        product = get_object_or_404(Product, id=id)
        if request.method=="POST":
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                product = form.save(commit=False)
                product.created_date = timezone.now()
                product.save()
                return redirect('shop:product_detail', id=product.id)
        else:
            form = ProductForm(instance=product)
        return render(request, 'shop/product_edit.html', {'form': form})
    except HTTPError as err:
        if err.code == 404:
            return render(request, 'shop/404.html')
        if err.code == 400:
            return render(request, 'shop/404.html')
        if err.code == 500:
            return render(request, 'shop/500.html',)
        else:
            raise

def product_delete(request, id):
    try:
        product = get_object_or_404(Product, id=id)
        deleted = request.session.get('deleted', 'empty')
        request.session['deleted'] = product.name
        product.delete()
        return redirect('shop:product_list' )
    except HTTPError as err:
        if err.code == 404:
            return render(request, 'shop/404.html')
        if err.code == 400:
            return render(request, 'shop/404.html')
        if err.code == 500:
            return render(request, 'shop/500.html',)
        else:
            raise
            
def error_404_view(request, exception):
    return render(request, 'shop/404.html')
#function that gets called incase of a 500 internal server error.
def error_500_view(request):
    return render(request, 'shop/500.html')
