from django.db import models
from django.conf import settings


class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    employee_size = models.IntegerField(default=0)
    phone = models.CharField(max_length=14)
    website = models.URLField()

    def __str__(self):
        return self.name


class Favourite(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ManyToManyField(Company, null=True)

    def __str__(self):
        return str(self.id)

