# Generated by Django 4.1.5 on 2023-02-03 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_alter_course_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="information_about",
            options={"verbose_name": "Информациионные текста"},
        ),
        migrations.RemoveField(
            model_name="information_about",
            name="first_text",
        ),
        migrations.RemoveField(
            model_name="information_about",
            name="second_text",
        ),
        migrations.RemoveField(
            model_name="information_about",
            name="third_text",
        ),
    ]
