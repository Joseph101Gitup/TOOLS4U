from django.db import models

from AdminApp.models import tbl_location

# Create your models here.


class tbl_login(models.Model):
    loginid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    role = models.CharField(max_length=25)
    status = models.CharField(max_length=30)

class tbl_user(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=25)
    user_phone = models.BigIntegerField()
    user_email = models.CharField(max_length=60)
    user_location = models.ForeignKey(tbl_location,on_delete=models.CASCADE)
    user_landmark = models.CharField(max_length=40)
    user_pincode = models.BigIntegerField()
    user_regdate = models.DateField()
    user_loginid = models.ForeignKey(tbl_login,on_delete=models.CASCADE)  

class tbl_seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=25)
    seller_image = models.ImageField()
    seller_phone = models.BigIntegerField()
    seller_email = models.CharField(max_length=60)
    seller_location = models.ForeignKey(tbl_location,on_delete=models.CASCADE)
    seller_landmark = models.CharField(max_length=40)
    seller_pincode = models.BigIntegerField()
    seller_idproof = models.ImageField()
    seller_regdate = models.DateField()
    seller_loginid = models.ForeignKey(tbl_login,on_delete=models.CASCADE)  
    


