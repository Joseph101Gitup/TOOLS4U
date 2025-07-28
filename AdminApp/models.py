from django.db import models

# Create your models here.

class tbl_district(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=40)

class tbl_location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=40)
    district_id = models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=40)
    category_image = models.ImageField()

class tbl_subcategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    subcategory_name = models.CharField(max_length=40)
    subcategory_image = models.ImageField()
    category_id = models.ForeignKey(tbl_category,on_delete=models.CASCADE)



   