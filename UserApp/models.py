import datetime
from django.db import models

from GuestApp.models import tbl_user
from SellerApp.models import tbl_tool


class tbl_rentrequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    request_toolid = models.ForeignKey(tbl_tool,on_delete=models.CASCADE)  
    request_quantity = models.IntegerField()
    request_tprice = models.BigIntegerField()
    request_userid = models.ForeignKey(tbl_user,on_delete=models.CASCADE) 
    request_date = models.DateField() 
    request_requireddate = models.DateField()
    request_returndate = models.DateField()
    request_Remark = models.CharField(max_length=100,null=True)
    request_Status = models.CharField(max_length=20)


class tbl_purchaserequest(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    purchase_toolid = models.ForeignKey(tbl_tool,on_delete=models.CASCADE)  
    purchase_quantity = models.IntegerField()
    purchase_tprice = models.BigIntegerField()
    purchase_userid = models.ForeignKey(tbl_user,on_delete=models.CASCADE) 
    purchase_date = models.DateField() 
    purchase_stock = models.IntegerField()
    purchase_Status = models.CharField(max_length=20)


class tbl_purchasepayment(models.Model):
    ppayment_id = models.AutoField(primary_key=True)
    ppayment_amount = models.BigIntegerField()
    ppayment_userid = models.ForeignKey(tbl_user,on_delete=models.CASCADE) 
    ppayment_purchaserequestid = models.ForeignKey(tbl_purchaserequest,on_delete=models.CASCADE)
    ppayment_date = models.DateField()
    ppayment_status = models.CharField(max_length=30)


class tbl_rentpayment(models.Model):
    rpayment_id = models.AutoField(primary_key=True)
    rpayment_amount = models.BigIntegerField()
    rpayment_userid = models.ForeignKey(tbl_user,on_delete=models.CASCADE) 
    rpayment_rentrequestid = models.ForeignKey(tbl_rentrequest,on_delete=models.CASCADE)
    rpayment_date = models.DateField()
    rpayment_status = models.CharField(max_length=30)

# Create your models here.
