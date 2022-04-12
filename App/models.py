from django.db import models

class namaz_time_table (models.Model):
    namaz_name = models.CharField(max_length=50)
    namaz_time = models.CharField(max_length=50)

    def __str__(self):
        return self.namaz_name
    