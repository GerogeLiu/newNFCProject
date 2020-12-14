from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CustomerProfile(models.Model):
    customer = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)
    address = models.TextField()

    def __str__(self):
        return 'customer {}'.format(self.customer.username)


class EndUserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return 'End User {}'.format(self.endUser.username)

class EndUserInfo(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    school = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    aboutme = models.TextField(blank=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return "user:{}".format(self.user.username)
