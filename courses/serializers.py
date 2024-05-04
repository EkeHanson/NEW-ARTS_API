from rest_framework import serializers
from .models import Category, Course, Instructors

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructors
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    duration = serializers.CharField(default=' 2 hours')
    class Meta:
        model = Course
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    image = serializers.ImageField()

    class Meta:
        model = Category
        fields = '__all__'
