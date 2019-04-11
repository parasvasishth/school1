# Generated by Django 2.2 on 2019-04-11 09:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(blank=True, max_length=20, null=True)),
                ('username', models.CharField(default='', max_length=25, unique=True)),
                ('password', models.CharField(default='', max_length=30)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('area', models.CharField(blank=True, max_length=20, null=True)),
                ('pincode', models.PositiveIntegerField(blank=True, default='1', null=True)),
                ('landmark', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '8885559997'. Up to 12 digits allowed along with country code.", regex='^\\+?1?\\d{9,15}$')])),
                ('website', models.URLField(blank=True, null=True)),
                ('principal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='schoolprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MediaUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='')),
                ('video1', models.URLField(blank=True, null=True)),
                ('video2', models.URLField(blank=True, null=True)),
                ('school_brouche', models.FileField(blank=True, null=True, upload_to='')),
                ('SchoolProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MediaUpload', to='account.SchoolProfile')),
            ],
        ),
    ]
