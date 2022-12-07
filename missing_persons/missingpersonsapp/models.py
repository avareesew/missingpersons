from django.db import models

# Create your models here.
class Missing_Person(models.Model):
    date_missing = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    firstName = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=1)

    def __str__(self):
        return self.lastName + self.firstName

    class Meta :
        db_table = "Missing Persons"