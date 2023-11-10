from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    roll_no = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class ReferenceFace(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reference_faces/')

    def __str__(self):
        return f"Reference face for {self.student.name}"

