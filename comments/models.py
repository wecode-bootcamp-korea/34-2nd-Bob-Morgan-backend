from django.db import models

from places.models import Place
from users.models  import User
from core.models   import TimeStampModel

class Comment(TimeStampModel):
    content    = models.CharField(max_length=500)
    deleted_at = models.DateTimeField(null=True)
    place      = models.ForeignKey(Place, on_delete=models.CASCADE)
    user       = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'
