# Generated by Django 5.0.6 on 2024-05-18 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='contacts',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='github_url',
            field=models.CharField(blank=True, help_text='Link to owners github', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linkedin_url',
            field=models.CharField(blank=True, help_text='Link to owners linked in', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='youtube_url',
            field=models.CharField(blank=True, help_text='Link to owners youtube', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
