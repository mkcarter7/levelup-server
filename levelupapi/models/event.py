from  .gamer import Gamer
from django.db import models
from .game import Game

class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE)  # One-to-Many with Gamer
    date = models.DateField()
    time = models.TimeField()
