from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from django.db.models.signals import post_save
from django_jalali.db import models as jmodels
import jdatetime

class shippingdress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    shipping_full_name = models.CharField(max_length=250)
    shipping_email=models.CharField(max_length=300)
    shipping_phone=models.CharField(max_length=25 ,blank=True)
    shipping_address1=models.CharField(max_length=250 ,blank=True)
    shipping_address2=models.CharField(max_length=250,blank=True, null=True)
    shipping_city=models.CharField(max_length=25 ,blank=True)
    shipping_state=models.CharField(max_length=25 ,blank=True)
    shipping_zipcode=models.CharField(max_length=25 ,blank=True)
    shipping_countary=models.CharField(max_length=25 ,default='Iran')
    

    class Meta:
        verbose_name_plural='shippingdress'

    def __str__(self):
        return f"shipping adress From{self.shipping_full_name}"
    
    def __str__(self):
        return self.user.username
    

def create_shopping_user(sender, instance, created, **kwargs):
    if created:
        user_shopping=shippingdress(user=instance)
        user_shopping.save()
post_save.connect(create_shopping_user,sender=User)
    
class order(models.Model):
    STATUS_ORDER=[
        ('pending','waiting to pay'),
         ('processing','waiting to process'), 
         ('shipped','sending to post'),
          ('delivered','is delivered'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name=models.CharField(max_length=250)
    email=models.EmailField(max_length=300)
    shipping_adress=models.TextField(max_length=150000)
    amount_paid=models.DecimalField(decimal_places=0, max_digits=12)
    date_ordered=jmodels.jDateTimeField(auto_now=True) 
    status=models.CharField(max_length=50,choices=STATUS_ORDER,default='pending')
    last_update=jmodels.jDateField(auto_now=True)

    def save(self,*args,**kwargs):
        if self.pk:
            old_status=order.objects.get(id=self.pk).status
            if old_status !=self.status:
                self.last_update=jdatetime.datetime.now()
        super().save(*args,**kwargs)



    def __str__(self):
        return f'order - {str(self.id)}'
    
class orderitem(models.Model):
    order=models.ForeignKey(order,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    uaer=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    quantity =models.PositiveBigIntegerField(default=1)
    price=models.DecimalField(decimal_places=0, max_digits=12)

    def __str__(self):
        if self.user is not None:
            return f'order Item - {str(self.id)} for {self.user }'
        else:
            return f'order Item - {str(self.id)}'


