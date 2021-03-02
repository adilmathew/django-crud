from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime
# Create your models here.
User=get_user_model()
class Rfq(models.Model):
    rfq_id = models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.RESTRICT)
    create_date=models.DateTimeField(editable=False)#remember to save date while saving
    deadline=models.DateField()#we allow user to chnge deadline
    targetdate=models.DateTimeField()
    description=models.TextField()
    attachment=models.URLField()
    LISTING=[
        ('PVT','VENDOR_GROUP'),
        ('PUB','PUBLICLY'),
    ]
    rfq_reach=models.CharField(max_length=3,choices=LISTING)
    PRIORITY_LIST=[
        ('PRT','PRIORITY'),
        ('AOG','AOG'),
        ('NOR','NORMAL')
    ]
    preference=models.CharField(max_length=3,choices=PRIORITY_LIST)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.rfq_id:
            self.create_date = timezone.now()
        return super(Rfq, self).save(*args, **kwargs)




class Component(models.Model):
    component_id=models.AutoField(primary_key=True)
    COMPONENT_TYPE=[
        ('P','PARTS'),
        ('C','CONSUMABLES'),
    ]
    component_type=models.CharField(max_length=1,choices=COMPONENT_TYPE)
    rfq_id=models.ForeignKey('Rfq',on_delete=models.PROTECT)
 
class Part(models.Model):
    part_id=models.AutoField(primary_key=True)
    part_name=models.CharField(max_length=50)
    part_number=models.CharField(max_length=20)
    quantity=models.IntegerField()
    description=models.TextField()
    manufacturer=models.CharField(max_length=100,default="others")
    component_id=models.ForeignKey('Component',on_delete=models.CASCADE)
    
 
class Consumable(models.Model):
    consumable_id=models.AutoField(primary_key=True)
    part_number=models.CharField(max_length=20)
    consumable_name=models.CharField(max_length=50)
    description=models.TextField()
    quantity=models.IntegerField()
    manufacturer=models.CharField(max_length=100,default="others")
    component_id=models.ForeignKey('Component',on_delete=models.CASCADE)