from django.db import models

from places.models import Place
from users.models  import User
from core.models   import TimeStampModel

class Reservation(TimeStampModel):
    reservation_date = models.DateField()
    under_name       = models.CharField(max_length=30)
    number_of_people = models.IntegerField()
    request          = models.CharField(max_length=500, default='')
    place            = models.ForeignKey(Place, on_delete=models.CASCADE)
    timeline         = models.ForeignKey('Timeline', on_delete=models.CASCADE)
    user             = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reservations'

class Timeline(models.Model):
    time = models.TimeField()

    class Meta:
        db_table = 'timelines'

    @property
    def hh_mm(self):
        return self.time[:5]
