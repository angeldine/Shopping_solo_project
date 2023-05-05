from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey('shop.Product', on_delete=models.SET_NULL, null=True, related_name='carts')
    quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product},{self.quantity},{self.created_date}'

# switch customer to user so that we can use Django's componenents
# https://blog.crunchydata.com/blog/extending-djangos-user-model-with-onetoonefield 
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name}, {self.user.email}, {self.address}'

    class Meta:
        db_table = 'customer'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.customer.save()

class LineItem(models.Model):
    quantity = models.IntegerField(default=0, null=True, blank=True)
    product = models.ForeignKey('shop.Product', on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey('shop.Cart', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey('shop.Order', on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity},{self.product},{self.cart},{self.order},{self.created_date}'
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class Order(models.Model):
    customer = models.ForeignKey('shop.Customer', on_delete=models.SET_NULL, null=True )
    complete = models.BooleanField(default=False) 
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer},{self.created_date}, {self.id}'
    
    @property
    def shipping(self):
        shipping = False
        lineitems = self.lineitem_set.all()
        return shipping
    
    @property
    def get_cart_total(self):
        lineitems = self.lineitem_set.all()
        total = sum([item.get_total for item in lineitems])
        return total
    
    @property
    def get_cart_items(self):
        lineitems = self.lineitem_set.all()
        total = sum([item.quantity for item in lineitems])
        return total


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    category = models.CharField(null=True, max_length=200, db_index=True)
    sub_category = models.CharField(null=True,max_length=200, db_index=True)
    product_number = models.CharField(null=True, max_length=200, db_index=True)
    image = models.ImageField(null=True, blank=True)
    quantity =  models.IntegerField(default=0, null=True, blank=True)
    profit = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name},{self.price},{self.category},{self.sub_category},{self.product_number},{self.image},{self.created_date}'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.city

    