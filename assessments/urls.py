from django.urls import path
from .views import AssessmentListCreateAPIView, AssessmentDetailAPIView

urlpatterns = [
    path('', AssessmentListCreateAPIView.as_view(), name='assessment-list-create'),
    path('<int:pk>/', AssessmentDetailAPIView.as_view(), name='assessment-detail'),
]
