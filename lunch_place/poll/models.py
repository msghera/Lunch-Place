from django.db import models
from restaurant.models import Menu
from model_utils import Choices
from django.contrib.auth.models import User

POLL_TYPE = Choices(
    ("running",  'running'),
    ("finished", 'finished'),
)


class Poll(models.Model):
    start_datetime = models.DateTimeField(null=True)
    end_datetime = models.DateTimeField(null=True)
    poll_date = models.DateField(auto_now_add=True, null=False)
    winner_menu_id = models.ForeignKey(
        Menu,
        on_delete=models.DO_NOTHING,
        null=True
    )
    status = models.CharField(
        max_length=10,
        choices=POLL_TYPE,
        default="running"
    )

    class Meta:
        ordering = ['-poll_date']


class Vote(models.Model):
    poll_id = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        null=False
    )
    menu_id = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        null=False
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False
    )
    created = models.DateTimeField(auto_now_add=True, null=False)
