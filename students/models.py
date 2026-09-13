from django.db import models
class Student(models.Model):
    STATUS =[("Registered","Registered"),]("Pending","Pending"),
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    workshop = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS, default="Registered")

def __str__(self):
    return self.name