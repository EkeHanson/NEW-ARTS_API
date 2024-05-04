from django.contrib import admin
from .models import Category, Course, Instructors


@admin.register(Instructors)
class InstructorsAdmin(admin.ModelAdmin):
    list_display = ('instructor_id', 'email', 'instructor_first_name', 'instructor_last_name', 
                    'courses_assigned', 'number_of_students')
    list_filter = ('instructor_first_name', 'instructor_id')
    search_fields = ('email',)
  


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'amount', 'duration')
    list_filter = ('category', 'duration')
    search_fields = ('title',)
