from django.db import models

class Favourites(models.Model):
    title = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title
