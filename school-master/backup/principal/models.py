from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save ,post_save
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length = 255 )
    slug = models.SlugField()
    content = models.TextField()
    # image = mod File Field
    status = models.BooleanField(default=False)
    #relations
    created_by=models.ForeignKey(User,related_name='message_created_by',on_delete= models.SET_NULL,null=True)
    updated_by = models.ForeignKey(User,related_name='message_updated_by',on_delete=models.SET_NULL,null=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    def save(self):
        user = get_current_authenticated_user()
        if self.id:
            self.updated_by =user;
        else:
            self.created_by =user;
            self.updated_by =user;
        return super(Message,self).save()
    
def save_message(sender, instance,*args, **kwargs):
    if instance.status:
        messages = Message.objects.filter(status=True).exclude(id=instance.id)
        for message in messages:
            message.status=False
            message.save()
    


post_save.connect(save_message,sender=Message)
