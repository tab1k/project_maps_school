from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150, blank=False)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="photo/category/", blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"





