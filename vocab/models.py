from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom


class Mot(models.Model):
    terme = models.CharField(max_length=200)
    definition = models.TextField()
    exemple = models.TextField(blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.terme