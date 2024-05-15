from rest_framework import serializers
from .models import Assessment

class AssessmentSerializer(serializers.ModelSerializer):
    instructor_first_name = serializers.CharField(source='instructor.instructor_first_name')
    instructor_last_name = serializers.CharField(source='instructor.instructor_last_name')
    instructor_image = serializers.ImageField(source='instructor.image', read_only=True)

    class Meta:
        model = Assessment
        fields = ['id', 'user', 'course', 'instructor', 'score', 'comments', 'instructor_first_name', 'instructor_last_name', 'instructor_image']
        read_only_fields = ['instructor_first_name', 'instructor_last_name', 'instructor_image']
