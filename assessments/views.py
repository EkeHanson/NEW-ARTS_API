from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .models import Assessment
from .serializers import AssessmentSerializer

class AssessmentListCreateAPIView(APIView):
    def get(self, request):
        assessments = Assessment.objects.all()
        serializer = AssessmentSerializer(assessments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssessmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssessmentDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Assessment.objects.get(pk=pk)
        except Assessment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        assessment = self.get_object(pk)
        serializer = AssessmentSerializer(assessment)
        return Response(serializer.data)

    def put(self, request, pk):
        assessment = self.get_object(pk)
        serializer = AssessmentSerializer(assessment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        assessment = self.get_object(pk)
        assessment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
