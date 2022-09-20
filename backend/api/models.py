from django.db import models

# Create your models here.

class Students(models.Model):
    StudId = models.AutoField(primary_key=True)
    StudName = models.CharField(max_length=140)
    Course = models.CharField(max_length=140)
    Rating = models.IntegerField()

    def __str__(self):
        return self.StudName

    class Meta:
        ordering = ['StudId']
