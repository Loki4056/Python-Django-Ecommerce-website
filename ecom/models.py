from django.db import models
from django.contrib.auth.models import User
from django.db.models import BigAutoField
from django.apps import apps  # Import the apps module

# Create your models here.

class Customer(models.Model):
    id = BigAutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.FileField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class CartItem(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product_id = models.PositiveIntegerField()  # Store the product's ID
    quantity = models.PositiveIntegerField(default=1)

    def product(self):
        return apps.get_model('ecom', 'Product').objects.get(id=self.product_id)

    def __str__(self):
        return f"{self.user.username}'s cart item for {self.product().name}"
    
class Product(models.Model):
    id = BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    description=models.CharField(max_length=500)
    

    def __str__(self):
        return self.name


class Orders(models.Model):
    id = BigAutoField(primary_key=True)
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)

class Feedback(models.Model):
    id = BigAutoField(primary_key=True)
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name