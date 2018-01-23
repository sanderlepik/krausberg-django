from django.db import models


class JobOffer(models.Model):
    image = models.ImageField()
    position_et = models.CharField(max_length=50)
    intro_text_et = models.CharField(max_length=200)
    position_en = models.CharField(max_length=50)
    intro_text_en = models.CharField(max_length=200)
    position_ru = models.CharField(max_length=50)
    intro_text_ru = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.position_et
