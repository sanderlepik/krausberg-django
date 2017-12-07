from django.db import models

# Create your models here.


class job_offers(models.Model):
    position = models.CharField(max_length=50)
    intro_text = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.position
