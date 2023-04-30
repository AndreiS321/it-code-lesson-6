from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Lastname: {self.last_name} name: {self.name} email: {self.email}"
