from django.db import models

from AdminApp.models import tbl_category, tbl_subcategory
from GuestApp.models import tbl_seller



class tbl_tool(models.Model):
    tool_id = models.AutoField(primary_key=True)
    tool_name = models.CharField(max_length=25)
    tool_photo = models.ImageField()
    tool_subcategory = models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE, null=True, default=None)
    tool_price = models.FloatField()
    tool_discription = models.CharField(max_length=100)
    tool_seller = models.ForeignKey(tbl_seller,on_delete=models.CASCADE)
    tool_stock = models.IntegerField()
    tool_status = models.CharField(max_length=25)
    tool_type = models.CharField(max_length=25)

# Create your models here.
