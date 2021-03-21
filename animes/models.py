from django.db import models

class Animes(models.Model):
    animeName = models.CharField(max_length=50)
    produtora = models.CharField(max_length=50)
    lancamento = models.IntegerField()
    sinopse = models.CharField(max_length=200)