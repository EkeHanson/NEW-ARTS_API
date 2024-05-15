from django.db import models
from django.utils import timezone
from registration.models import CustomUser, EnrolledCourse
from courses.models import  Course

class Assessment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    schedule_date = models.DateTimeField()
    score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    feedback = models.TextField(blank=True)
    assessments = models.JSONField()

    @property
    def instructor(self):
        instructor_instance = self.enrolled_course.course.instructor_id
        return {
            'first_name': instructor_instance.instructor_first_name,
            'last_name': instructor_instance.instructor_last_name,
            'image_url': instructor_instance.image.url if instructor_instance.image else None
        }

    def __str__(self):
        if self.user:
            return f"Assessment for {self.user.email} on {self.enrolled_course.course.title} with {self.instructor['first_name']} {self.instructor['last_name']}"
        else:
            return f"Assessment on {self.enrolled_course.course.title}"

    def administer_assessment(self, user_answers, user=None):
        self.user = user
        # Compare user's answers with correct answers and calculate the score
        correct_answers = [question['correct_answer'] for question in self.assessments]
        user_score = sum([1 for user_answer, correct_answer in zip(user_answers, correct_answers) if user_answer == correct_answer])
        
        # Calculate the score percentage
        self.score = (user_score / len(correct_answers)) * 100

        # Save the assessment
        self.save()

        return self.score
