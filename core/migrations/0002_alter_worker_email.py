# Generated by Django 3.2.3 on 2023-04-30 15:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worker",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
