from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Appeal(models.Model):
    STATUSES = (
        (0, 'new'),
        (1, 'in progress'),
        (2, 'done'),
    )

    id = models.IntegerField(primary_key=True, verbose_name='id')
    number = models.IntegerField(null=False, unique=True, verbose_name='appeal number')
    created_at = models.DateTimeField(default=now(), verbose_name='created at')
    description = models.CharField(max_length=256, verbose_name='description')
    creator = models.ForeignKey(User, null=False, verbose_name='appeal creator', on_delete=models.CASCADE)
    status = models.IntegerField(default=0, choices=STATUSES, verbose_name='status')
