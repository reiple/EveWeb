from django.db import models

# Create your models here.


class BoardCategory(models.Model):
    Title = models.CharField(max_length=40, null=False)
    
class BoardEntry(models.Model):
    Title = models.CharField(max_length=80, null=False)
    Content = models.TextField(null=False)
    Created = models.DateTimeField(auto_now_add=True, auto_now=True)
    Category = models.ForeignKey(BoardCategory)
    Comments = models.PositiveSmallIntegerField(default=0, null=True)
    
class BoardComment(models.Model):
    Name = models.CharField(max_length=20, null=False)
    Content = models.TextField(max_length=2000, null=False)
    Created = models.DateTimeField(auto_now_add=True, auto_now=True)