from django.db import models
from django.contrib.auth.models import User
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=255)
    amount =  models.IntegerField()
    description = models.TextField()
    code = models.IntegerField()
    price = models.IntegerField()
    