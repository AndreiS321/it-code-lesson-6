# Generated by Django 3.2.3 on 2023-04-30 14:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Worker",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("patronymic", models.CharField(max_length=100)),
                ("job", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
