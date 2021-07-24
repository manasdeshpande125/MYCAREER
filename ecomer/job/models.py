from django.db import models

# Create your models here.


class Index2(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

def __str__(self):
    return self.name




class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=40)
    desc = models.CharField(max_length=40)
    pub_date = models.DateField()

def __str__(self):
        return self.product_name
