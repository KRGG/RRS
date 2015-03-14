from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Location(models.Model):
    address = models.CharField(max_length=200)
    # Add geolocation field
    
    def __str__(self):
        return self.address

class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    # Add date and verified status
    
    def __str__(self):
        return self.name

class Cuisine(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class PriceRange(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class DressCode(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class PaymentOption(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    # Add image/s field
    
    area = models.ForeignKey('Area')
    location = models.ForeignKey('Location')
    price_range = models.ForeignKey('PriceRange')
    dress_code = models.ForeignKey('DressCode')
    
    payment_options = models.ManyToManyField('PaymentOption')
    cuisine = models.ManyToManyField('Cuisine')
    menu = models.ManyToManyField('Menu')
    
    operating_hours = models.TextField()
    contact_info = models.TextField(blank=True)
    parking_info = models.TextField(blank=True)
    additional_info = models.TextField(blank=True)
    website = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
# Restaurant statistics on restaurant module
# Reservation table pending time slot and limit discussion

    
