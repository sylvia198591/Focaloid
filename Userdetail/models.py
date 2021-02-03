# from django.db import models
from django.db import models

# Create your models here.
class Users(models.Model):
    Name=models.CharField(max_length=200)
    Accno=models.IntegerField()
    Telephone=models.IntegerField()
    Email = models.EmailField(max_length=254)
    Username = models.CharField(max_length=200,unique=True)
    Password = models.CharField(max_length=200)
    isActive=models.BooleanField(default=False)
    isLog = models.BooleanField(default=False)
    def __str__(self):
        return self.Username
# Create your models here.
