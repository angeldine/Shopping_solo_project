from django.urls import path, include
import django.contrib.auth.urls
from . import views

app_name = 'shop'

# the empty path '' becomes the 'home page
urlpatterns = [
        path('', views.products.product_list, name='product_list'),
        path('accounts/', include('django.contrib.auth.urls')),
        path('basket_add/<int:product_id>/', views.basket.basket_add, name ='basket_add'),
        path('basket_remove/<int:product_id>/', views.basket.basket_remove, name ='basket_remove'),
        path('basket_detail/', views.basket.basket_detail, name ='basket_detail'),
        path('signup/', views.signup, name='signup'),
        path('dashboard/', views.dashboard, name='dashboard'),
        path('customer_list', views.customers.customer_list, name='customer_list'),
        path('customer/<int:id>/', views.customers.customer_detail, name= 'customer_detail'),
        path('order_list/', views.orders.order_list, name='order_list'),
        path('order/<int:id>/', views.orders.order_detail, name= 'order_detail'),
        path('payment/', views.payment, name ='payment'),
       # path('product/buy/', views.product_buy, name='product_buy'),
        path('product_list/', views.product_list, name='product_list'),
        path('product/<int:id>/', views.products.product_detail, name= 'product_detail'),
        path('product_new/', views.products.product_new, name= 'product_new'),
        path('product/<int:id>/edit/', views.products.product_edit, name= 'product_edit'),
        path('product/<int:id>/delete/', views.products.product_delete, name= 'product_delete'),
        path('purchase/', views.purchase, name ='purchase'),
        path('update_item/',views.orders.updateItem, name='update_item'),
        path('cartlist/', views.orders.cartList, name='cartlist'),
        path('checkout/', views.orders.checkout, name='checkout'),
        path('process_order/', views.orders.processOrder, name="process_order"),
        path('error/', views.products.error_404_view, name="error")
       # path('linechart/', views.products.line, name='linechart'),

        ]
        #handling the 404 error, calling the corresponding view function incase of error.
handler404 = 'shop.views.products.error_404_view'
#handling the 500 error, calling the corresponding view function incase of error.
handler500 = 'shop.views.error_500_view'
