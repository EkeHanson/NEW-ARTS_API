# Generated by Django 5.0.2 on 2024-05-04 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_instructors_courses_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructors',
            name='courses_list',
        ),
    ]
