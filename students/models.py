from django.db import models

# Create your models here.

class Student(models.Model):
    
    gender_choice = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    student_number = models.IntegerField()
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/')
    full_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    gender = models.CharField(choices=gender_choice, max_length=100)


    def __str__(self):
        return self.full_name