from django.db import models


# Create your models here.
class Phone(models.Model):
    brand = models.TextField()
    camera = models.IntegerField()
    ram = models.IntegerField()
    price = models.IntegerField()
    display = models.TextField()
    bluetooth = models.TextField()


class Apple(models.Model):
    kit = models.TextField()


class Samsung(models.Model):
    fastcharge = models.BooleanField()


class Asus(models.Model):
    nfs = models.BooleanField()

class Xiaomi(models.Model):
    hyroscope = models.BooleanField()
