# Generated by Django 4.1.6 on 2023-02-04 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0011_category_image_alter_subject_image"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Subject",
        ),
    ]
