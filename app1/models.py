from django.db import models


class Usertable(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=12)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=8)
    is_admin = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.firstname
