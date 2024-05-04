from django.urls import path
from . import views

urlpatterns = [

    path('add_course/<int:user_id>/<int:course_id>/', views.add_course_to_user, name='add_course_to_user'),
    path('remove_course/<int:user_id>/<int:course_id>/', views.remove_course_from_user, name='remove_course_from_user'),
    path('user_courses/<int:user_id>/', views.get_user_courses, name='get_user_courses'),
    path('course/<int:course_id>/users/', views.get_users_registered_for_course, name='get_users_registered_for_course'),

    path('send-registration-email/', views.send_registration_email, name='send_registration_email'),

    path('create/', views.CreateUserAPIView.as_view(), name='create_user'),

    path('create/<int:pk>/', views.UserDetailAPIView.as_view(), name='edit_user'),


    path('login/', views.LoginView.as_view(), name='login'),
    path('password/reset/', views.PasswordResetAPIView.as_view(), name='password_reset'),
    path('password/reset/confirm/', views.PasswordResetConfirmAPIView.as_view(), name='password_reset_confirm'),
]
