from django.db import models

# Create your models here.


class APIKey(models.Model):
    UserName = models.CharField(max_length=255, null=False)
    KeyID = models.CharField(max_length=255, null=False)
    VCode = models.CharField(max_length=255, null=False)
    Created = models.DateTimeField(auto_now_add=True, auto_now=True)
    
    
class WormholeMemer(models.Model):
    UserName = models.CharField(mal_length=255, null=False)
    CheckDate = models.DateTimeField(auto_now_add=True, auto_now=True)
    
    
    