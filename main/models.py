from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150, blank=False)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)




    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Information_About(models.Model):
    """ ОСНОВНАЯ ИНФОРМАЦИЯ НА СТРАНИЦЕ """
    first_text = models.TextField("Информационный текст1")
    second_text = models.TextField("Информационный текст2")
    third_text = models.TextField("Информационный текст3")


class Subject(models.Model):
    """ Предметы """
    name = models.CharField("Название", max_length=100, blank=False)
    price = models.IntegerField("Цена", default=20000, blank=True)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Изображение", upload_to="subjects/", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Many to One

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"






