from rest_framework import serializers
from .models import Category, Course, Instructors



class CourseSerializer(serializers.ModelSerializer):
    duration = serializers.CharField(default=' 2 hours')
    number_of_students = serializers.IntegerField(default= 0)
    class Meta:
        model = Course
        fields = '__all__'
        extra_kwargs = {
        'course_code': {'max_length': 25} # Make instructor_id optional
    }
        
class InstructorSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Instructors
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    image = serializers.ImageField()

    class Meta:
        model = Category
        fields = '__all__'
