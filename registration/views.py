from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.http import Http404
from .serializers import LoginSerializer
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import secrets
import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import CustomUser, Course, EnrolledCourse


def add_course_to_user(request, user_id, course_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    course = get_object_or_404(Course, pk=course_id)
    
    # Assuming you want to set enrolled_courses to True for this course
    course.enrolled_courses = True
    course.number_of_students += 1
    course.save()

    user.enrolled_courses.add(course)
    return JsonResponse({'message': 'Course added to user successfully'})

def remove_course_from_user(request, user_id, course_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    course = get_object_or_404(Course, pk=course_id)
    user.enrolled_courses.remove(course)
    return JsonResponse({'message': 'Course removed from user successfully'})

from django.core.serializers import serialize

def get_user_courses(request, user_id): 
    user = get_object_or_404(CustomUser, pk=user_id)
    user_courses = user.enrolled_courses.all()
    course_data = []
    for course in user_courses:
        course_info = {
            'courseId': course.instructor_id_id,  # Use the ID of the instructor instead of the object
            'title': course.title,
            'details': course.details,
            'days_per_week': course.days_per_week,
            'duration': course.duration,
        }
        # Get instructor details
        instructor = course.instructor_id
        if instructor:  # Check if instructor exists
            course_info['instructor'] = {
                'id': instructor.id,
                'first_name': instructor.instructor_first_name,
                'instructor_image_url': instructor.image.url if instructor.image else None,
                'last_name': instructor.instructor_last_name,
            }
        course_data.append(course_info)
    return JsonResponse({'courses': course_data})


def get_users_registered_for_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrolled_courses = EnrolledCourse.objects.filter(course=course)  # Get all enrollments for the course

    user_data = []
    for enrollment in enrolled_courses:
        user_info = {
            'email': enrollment.user.email,
            'first_name': enrollment.user.first_name,
            'last_name': enrollment.user.last_name,
            'course_id': course.id,
            'course_title': course.title,
            'registration_date': enrollment.registration_date.strftime('%Y-%m-%d %H:%M:%S')
        }
        user_data.append(user_info)

    return JsonResponse({'users': user_data})


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        print("Received email:", email)
        print("Received password:", password)

        # Authenticate using email and password
        user = authenticate(email=email, password=password)

        if user:
            print("User authenticated successfully:", user)
            # If authentication is successful, generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'user_id': user.id,
                'user_email': user.email,
                'user_type': user.user_type,
                'user_first_name': user.first_name,
                'user_last_name': user.last_name
                # Add more user details if needed
            })
        else:
            print("Authentication failed for email:", email)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def send_registration_email(request):
#docg qver jlgv ywyy
    if request.method == 'POST':
        print("Email Tag!")
        print(request.data)  # Debug statement to print request.data
        email = request.data.get('email')  # Get email from JSON data
        first_name = request.data.get('first_name')  # Get email from JSON data
        last_name = request.data.get('last_name')  # Get email from JSON data
        print(email)  # Debug statement to print email
        if email:
            # You can customize the email subject and message as needed
            subject = 'Registration Confirmation'
            message = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Confirmation</title>
    <style>
        /* Define your CSS styles here */
        body {{
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 20px;
        }}
        .content {{
            padding: 20px;
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            background-color: #87ceeb;
            color: #ffffff;
            text-decoration: none;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h3>Welcome to The Arts Training</h3>
            <img src="https://artstraining.co.uk/img/site-logo.png" alt="Arts Training Logo" width="150">
        </div>
        <div class="content">
            <h3>Hi {first_name},<h3/>
            <p>Thank you for signing up with Arts Training.<br> Please click the button below to complete your registration.</p>
            <a href='https://artstraining.co.uk/complete-signup.html?first_name={first_name}&last_name={last_name}&email={email}' class="button">Complete Registration</a>
            <p>If you did not request for this registration, please ignore this email.</p>

            <p>Thank you, <br> The Arts Training Team</p>
        </div>
    </div>
</body>
</html>
'''

            recipient_list = [email]
            from_email = 'Do not reply Admin@artstraining.co.uk '  # Set the no-reply email address
            send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=message)
            print('Email sent successfully')
            return Response({'message': 'Email sent successfully'})
        else:
            return Response({'error': 'Email not provided in POST data'}, status=400)
    else:
        return Response({'error': 'Invalid request method'}, status=400)


class JWTExampleView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'You are authenticated'}
        return Response(content)

class CreateUserAPIView(APIView):
    def get(self, request: Request):

        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        # return Response(data='No user found', status=status.HTTP_404_NOT_FOUND)


    def post(self, request: Request):
        print("Created a User!")
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPIView(APIView):
    """
    API view to handle retrieving, updating, or deleting a single instructor.
    """

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve an existing instructor.
        """
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update an existing instructor.
        """
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Partially update an existing instructor.
        """
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
def generate_reset_token():
    return secrets.token_urlsafe(16)

def send_reset_email(user):
    reset_token = generate_reset_token()
    user.reset_token = reset_token
    print(user.reset_token)
    user.reset_token_expires = timezone.now() + datetime.timedelta(hours=10)  # Token expires in 3 hours
    user.save()
    reset_url = f'https://artstraining.co.uk/forgot-password-main.html?reset_token={reset_token}&amp;email={user.email}'
    
    subject = 'Password Reset'
    
    message =  f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Confirmation</title>
    <style>
        /* Define your CSS styles here */
        body {{
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 20px;
        }}
        .content {{
            padding: 20px;
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            background-color: #87ceeb;
            color: #ffffff;
            text-decoration: none;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h3>Welcome to The Arts Training</h3>
            <img src="https://artstraining.co.uk/img/site-logo.png" alt="Arts Training Logo" width="150">
        </div>
        <div class="content">
            <h3>Hi {user.first_name},<h3/>
            <br>
            <a href='{reset_url}' class="button">Click this link to reset your password</a>
            <p>This link will expire in 1 hour</p>
        </div>
    </div>
</body>
</html>'''

    from_email = 'Do not reply'  # Update with your email address
    recipient_list = [user.email]  # Send email to the user's email address

    send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=message)

class PasswordResetAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = CustomUser.objects.get(email=email)
        except ObjectDoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except MultipleObjectsReturned:
            return Response({'error': 'Multiple users found with this email'}, status=status.HTTP_400_BAD_REQUEST)
        
        send_reset_email(user)
        return Response({'message': 'Password reset link sent'}, status=status.HTTP_200_OK)

class PasswordResetConfirmAPIView(APIView):
    def post(self, request):
        reset_token = request.data.get('reset_token')
        email = request.data.get('email')
        password = request.data.get('password')

        # Retrieve the user based on the reset_token and email
        try:
            user = CustomUser.objects.get(email=email, reset_token=reset_token)
        except ObjectDoesNotExist:
            return Response({'error': 'Invalid reset token or email'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the reset token is expired
        if user.reset_token_expires < timezone.now():
            return Response({'error': 'Reset token has expired'}, status=status.HTTP_400_BAD_REQUEST)

        # Set the new password
        user.set_password(password)
        user.reset_token = None
        user.reset_token_expires = None
        user.save()

        return Response({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)