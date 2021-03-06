# Generated by Django 2.1.2 on 2018-10-05 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finderApp', '0002_auto_20181005_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialties', models.CharField(max_length=100)),
                ('ratings', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('stories', models.CharField(max_length=100)),
                ('photo_url', models.TextField()),
                ('numbers', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_points', models.IntegerField(default=-1)),
                ('their_points', models.IntegerField(default=-1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('my_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finderApp.Choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finderApp.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
