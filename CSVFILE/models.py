from django.db import models

class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    position=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name



