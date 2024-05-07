from django.urls import path
from . import views
urlpatterns = [

    path('assign_course_to_instructor/<int:course_id>/<int:instructor_id>/', views.assign_course_to_instructor, name='assign_course_to_instructor'),
    path('remove_course_from_instructor/<int:course_id>/<int:instructor_id>/', views.remove_course_from_instructor, name='remove_course_from_instructor'),
    path('assign_instructor_to_course/<int:instructor_id>/<int:course_id>/', views.assign_instructor_to_course, name='assign_instructor_to_course'),
    path('remove_instructor_from_course/<int:instructor_id>/<int:course_id>/', views.remove_instructor_from_course, name='remove_instructor_from_course'),


    path('instructors/', views.InstructorsCreateAPIView.as_view(), name='instructors-list'),
    path('instructors/<int:pk>/', views.InstructorDetailAPIView.as_view(), name='instructor-detail'),

    
    path('categories/', views.CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view(), name='category-detail'),

    path('', views.CourseListAPIView.as_view(), name='course-list'),
    path('<int:pk>/', views.CourseDetailAPIView.as_view(), name='course-detail'),

    path('courses/by_category/<int:category_id>/', views.CourseByCategoryAPIView.as_view(), name='courses_by_category'),
    
    path('enrolled/', views.EnrolledCourseAPIView.as_view(), name='enrolled-courses'),

]
