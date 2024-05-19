# Generated by Django 5.0.6 on 2024-05-19 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_customuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecoverySecret',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('secret', models.CharField(blank=True, max_length=6)),
            ],
        ),
    ]