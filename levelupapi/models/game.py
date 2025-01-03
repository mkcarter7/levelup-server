from  .gamer import Gamer
from .game_type import GameType
from django.db import models

class Game(models.Model):
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)         
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE) 
    skill_level = models.PositiveSmallIntegerField()       
    number_of_players = models.PositiveSmallIntegerField()
