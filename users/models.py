from django.db import models

from places.models import Place
from core.models   import TimeStampModel

class User(TimeStampModel):
    email             = models.CharField(max_length=80, null=True, unique=True)
    password          = models.CharField(max_length=200, null=True)
    nickname          = models.CharField(max_length=80, null=True)
    profile_image_url = models.CharField(max_length=1000, default='https://cdn-icons-png.flaticon.com/512/1450/1450252.png')
    date_of_birth     = models.DateField(null=True)
    platform          = models.ForeignKey('Platform', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'users'

class WishList(TimeStampModel):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user  = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'wish_lists'

class Platform(models.Model):
    serial_number  = models.BigIntegerField()
    social_network = models.ForeignKey('SocialNetwork', on_delete=models.CASCADE)

    class Meta:
        db_table = 'platforms'

class SocialNetwork(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'social_networks'
