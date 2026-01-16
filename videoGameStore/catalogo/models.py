from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    platform = models.CharField(max_length=200)
    image = models.CharField(max_length=200, default="logo.jpeg")

    def __str__(self):
        return self.name
