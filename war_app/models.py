from django.db import models

# Create your models here.
class Player(models.Model):
    num_cards = models.IntegerField()
    games_won = models.IntegerField()
