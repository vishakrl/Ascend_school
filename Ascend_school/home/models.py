from django.db import models

# Create your models here.


class students(models.Model):
    def __str__(self):
        return self.name
        

    admission_no=models.IntegerField(unique=True )
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=100)
    subject=models.CharField(max_length=30)
    guardian_name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    contact_detais=models.IntegerField(max_length=100)

