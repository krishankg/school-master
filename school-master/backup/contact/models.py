from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save ,post_save
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 255 )
    email = models.EmailField()
    phoneno = models.CharField(max_length = 255 )
    message = models.TextField()
    #relations
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    email = models.EmailField()
    phoneno = models.CharField(max_length = 255 )
    address = models.TextField()
    log= models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    status = models.BooleanField(default=False)
    created_by=models.ForeignKey(User,related_name='location_created_by',on_delete= models.SET_NULL,null=True)
    updated_by = models.ForeignKey(User,related_name='location_updated_by',on_delete=models.SET_NULL,null=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email

    def save(self):
        user = get_current_authenticated_user()
        if self.id:
            self.updated_by =user;
        else:
            self.created_by =user;
            self.updated_by =user;
        return super(Location,self).save()

def save_location(sender, instance,*args, **kwargs):
    if instance.status:
        locations = Location.objects.filter(status=True).exclude(id=instance.id)
        for location in locations:
            location.status=False
            location.save()
    


post_save.connect(save_location,sender=Location)