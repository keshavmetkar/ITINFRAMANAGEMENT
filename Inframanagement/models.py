from django.db import models

class Orgnization(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Location(models.Model):
    parent = models.ForeignKey(Orgnization, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

# Create your models here.
class PowerSource(models.Model):
    name = models.CharField(max_length=200)
    Office = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.name

class Ups(models.Model):
    name= models.CharField(max_length=200)
    source = models.ManyToManyField(PowerSource)
    Office = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.name

class Rack(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField()
    Office = models.ForeignKey(Location,on_delete=models.SET_NULL,blank=True,null=True)
    PowerSource= models.ManyToManyField(Ups, blank=True, null=True)

    def __str__(self):
        return self.name
