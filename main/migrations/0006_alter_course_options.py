# Generated by Django 4.1.5 on 2023-02-03 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_course"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course",
            options={"verbose_name": "Курс", "verbose_name_plural": "Курсы"},
        ),
    ]