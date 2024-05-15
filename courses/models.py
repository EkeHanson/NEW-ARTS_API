from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import random

class Instructors(models.Model):
    email = models.EmailField(max_length=80, unique=True)
    instructor_first_name = models.CharField(max_length=200)
    instructor_last_name = models.CharField(max_length=200)   
    courses_assigned = models.IntegerField(blank=True, null=True)
    number_of_students = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='instructor_images')
    instructor_id = models.CharField(max_length=8, unique=True, blank=True, null=True)
    
    def __str__(self):
        return f"{self.instructor_first_name} {self.instructor_last_name}"

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructors"

@receiver(pre_save, sender=Instructors)
def generate_instructor_id(sender, instance, *args, **kwargs):
    # Generate a random 8-digit number
    random_id = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    # Assign the generated ID to the instance
    instance.instructor_id = random_id

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images')
    details = models.TextField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    course_code = models.CharField(max_length=25)
    duration = models.CharField(max_length=45)
    days_per_week = models.PositiveIntegerField()
    enrolled_courses = models.BooleanField(default=False)
    number_of_students = models.IntegerField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    instructor_id = models.ForeignKey(Instructors, on_delete=models.CASCADE, related_name='courses')
    
   

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title
