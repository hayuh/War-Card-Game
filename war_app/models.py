from django.db import models

# Create your models here.
class Player(models.Model):

    games_won = models.IntegerField()
