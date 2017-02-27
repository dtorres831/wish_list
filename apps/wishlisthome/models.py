from __future__ import unicode_literals
from ..wishlist.models  import User
from django.db import models

# Create your models here.
class ItemManager(models.Manager):
    def itemreview(self, postdata, user):
        errors=[]
        if not postdata['item']:
            errors.append('no empty entries')
        if len(postdata['item'])<3:
            errors.append('item must be longer than 3 characters')
        response = {}
        if errors:
            response['Status']= False
            response['errors']= errors
        else:
            item = self.create(item=postdata['item'],user=user)
            response['Status']= True
            response['item'] = item
            
        return response

class Item(models.Model):
    item = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name="post")
    likeditems = models.ManyToManyField(User, related_name="likeditems")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ItemManager()
