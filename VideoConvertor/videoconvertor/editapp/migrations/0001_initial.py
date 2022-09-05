# Generated by Django 4.0.4 on 2022-06-08 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='profile')),
                ('DateOfBirth', models.DateField()),
                ('PhoneNumber', models.CharField(max_length=10)),
                ('Location', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('Cdate', models.DateTimeField(auto_now_add=True)),
                ('Udate', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
