# Generated by Django 5.0.6 on 2024-05-19 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_rename_file_courseitem_course_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesmodel',
            name='courses',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.courseitem'),
            preserve_default=False,
        ),
    ]
