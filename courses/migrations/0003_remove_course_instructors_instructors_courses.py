# Generated by Django 5.0.2 on 2024-05-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_course_instructor_course_instructors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='instructors',
        ),
        migrations.AddField(
            model_name='instructors',
            name='courses',
            field=models.ManyToManyField(related_name='instructors', to='courses.course'),
        ),
    ]
