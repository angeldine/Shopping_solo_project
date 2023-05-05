import csv
import os
from pathlib import Path
from django.db import models
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from decimal import *
import random


from shop.models import Cart, Customer, LineItem, Order, Product, ShippingAddress

class Command(BaseCommand):
    help = 'Load data into the tables'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
   
        Cart.objects.all().delete()
        LineItem.objects.all().delete()
        Order.objects.all().delete()
        Product.objects.all().delete()
        Customer.objects.all().delete()
        ShippingAddress.objects.all().delete()
        User.objects.all().delete()
        print("table dropped successfully")

        # create table again
        fake = Faker()
      

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/shop/dataset/data.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)
                
                first_name = row[6]
                last_name = row[7]
                
                user = User.objects.create_user(
                    first_name = first_name,
                    last_name = last_name,
                    username=fake.user_name(),
                    email=fake.ascii_free_email(), 
                    password='p@ssword'
                )
            
                customer = Customer.objects.get(user = user)
                customer.address = fake.address(),
                customer.address = str(customer.address[0])
                customer.save()
                
                # creating product details
                product = Product.objects.create(
                    name=row[17],
                    product_number=row[14],
                    price=Decimal(row[19]),
                    category=row[15],
                    sub_category=row[16],
                    image=row[18],
                    quantity = int(row[20]),
                    profit = Decimal(row[22])
                )
                product.save()

                customers = Customer.objects.filter(user = user)
                for customer in customers:  
                    order = Order.objects.create(
                    customer = customer,
                    )
                    order.save()
                    
                # create some carts 
                products = Product.objects.all()
                for product in products:
                    cart = Cart.objects.create(
                    product = product,
                    quantity = row[20],
                    )
                    cart.save()
            
                orders = Order.objects.filter(customer=customer)
                for order in orders:
                    line_item = LineItem.objects.create(
                    quantity = cart.quantity,
                    product = cart.product,
                    cart = cart,
                    order = order,
                    )
                    line_item.save()

                    shipping = ShippingAddress.objects.create(
                        address=fake.street_address(),
                        city=row[10],
                        state=row[11],
                        zipcode=row[12],
                        order=order
                    )
                    shipping.save()
                
                
                    
   