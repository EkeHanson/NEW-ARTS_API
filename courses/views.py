from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import JsonResponse
from .models import Category, Course, Instructors
from .serializers import CategorySerializer, CourseSerializer, InstructorSerializer

def assign_course_to_instructor(request, course_id, instructor_id):
    course = get_object_or_404(Course, pk=course_id)
    instructor = get_object_or_404(Instructors, pk=instructor_id)
    course.instructors.add(instructor)
    return JsonResponse({'message': f'Course "{course.title}" assigned to instructor "{instructor.instructor_first_name} {instructor.instructor_last_name}" successfully'})

def remove_course_from_instructor(request, course_id, instructor_id):
    course = get_object_or_404(Course, pk=course_id)
    instructor = get_object_or_404(Instructors, pk=instructor_id)
    course.instructors.remove(instructor)
    return JsonResponse({'message': f'Course "{course.title}" removed from instructor "{instructor.instructor_first_name} {instructor.instructor_last_name}" successfully'})

def assign_instructor_to_course(request, instructor_id, course_id):
    instructor = get_object_or_404(Instructors, pk=instructor_id)
    course = get_object_or_404(Course, pk=course_id)
    instructor.courses.add(course)
    return JsonResponse({'message': f'Instructor "{instructor.instructor_first_name} {instructor.instructor_last_name}" assigned to course "{course.title}" successfully'})

def remove_instructor_from_course(request, instructor_id, course_id):
    instructor = get_object_or_404(Instructors, pk=instructor_id)
    course = get_object_or_404(Course, pk=course_id)
    instructor.courses.remove(course)
    return JsonResponse({'message': f'Instructor "{instructor.instructor_first_name} {instructor.instructor_last_name}" removed from course "{course.title}" successfully'})


class CourseByCategoryAPIView(APIView):
    def get(self, request, category_id):
        try:
            # Get the category object
            category = Category.objects.get(pk=category_id)
            # Get all courses related to the category
            courses = Course.objects.filter(category=category)
            # Serialize the courses data
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class EnrolledCourseAPIView(APIView):
    def get(self, request):
        courses = Course.objects.filter(enrolled_courses=True)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        # Toggle the enrolled field
        course.enrolled = not course.enrolled
        course.save()
        serializer = CourseSerializer(course)
        return Response(serializer.data)

class InstructorsCreateAPIView(APIView):
    """
    API view to handle CRUD operations for Instructors.
    """

    def get(self, request):
        """
        Get a list of all instructors.
        """
        instructors = Instructors.objects.all()
        serializer = InstructorSerializer(instructors, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new instructor.
        """
        serializer = InstructorSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("serializer.errors")
        print(serializer.errors)
        print("serializer.errors")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class InstructorDetailAPIView(APIView):
    """
    API view to handle retrieving, updating, or deleting a single instructor.
    """

    def get_object(self, pk):
        try:
            return Instructors.objects.get(pk=pk)
        except Instructors.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve an existing instructor.
        """
        instructor = self.get_object(pk)
        serializer = InstructorSerializer(instructor)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update an existing instructor.
        """
        instructor = self.get_object(pk)
        serializer = InstructorSerializer(instructor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Partially update an existing instructor.
        """
        instructor = self.get_object(pk)
        serializer = InstructorSerializer(instructor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("serializer.errors")
        print(serializer.errors)
        print("serializer.errors")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailAPIView(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CourseListAPIView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("serializer.errors")
        print(serializer.errors)
        print("serializer.errors")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailAPIView(APIView):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
