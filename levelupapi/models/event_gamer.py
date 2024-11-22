from django.db import models
from .event import Event
from .gamer import Gamer

class EventGamer(models.Model):
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)  # Foreign key to Gamer
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
