
from django.db import models

class Place(models.Model):
    name                         = models.CharField(max_length=100)
    address                      = models.CharField(max_length=200)
    phone_number                 = models.CharField(max_length=50, default='')
    opening_hours                = models.CharField(max_length=200, default='')
    description                  = models.CharField(max_length=1000, default='')
    maximum_number_of_subscriber = models.IntegerField()
    latitude                     = models.DecimalField(max_digits=11, decimal_places=8)
    longitude                    = models.DecimalField(max_digits=11, decimal_places=8)
    able_to_reserve              = models.BooleanField()
    closed_temporarily           = models.BooleanField()
    category                     = models.ForeignKey('Category', on_delete=models.CASCADE)
    region                       = models.ForeignKey('Region', on_delete=models.CASCADE)
    menus                        = models.ManyToManyField('Menu', through='PlaceMenu', related_name='places')

    class Meta:
        db_table = 'places'

class PlaceMenu(models.Model):
    menu          = models.ForeignKey('Menu', on_delete=models.CASCADE)
    place         = models.ForeignKey('Place', on_delete=models.CASCADE)
    price         = models.ForeignKey('Price', on_delete=models.CASCADE)
    is_signature  = models.BooleanField()

    class Meta:
        db_table = 'places_menus'

class Menu(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'menus'

class Price(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=0)

    class Meta:
        db_table = 'prices'

class Category(models.Model):
    name  = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'

class Image(models.Model):
    image_url  = models.CharField(max_length=1000)
    place      = models.ForeignKey('Place', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Region(models.Model):
    name  = models.CharField(max_length=50)

    class Meta:
        db_table = 'regions'


