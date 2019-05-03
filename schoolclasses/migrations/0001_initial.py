# Generated by Django 2.2 on 2019-05-03 10:47

import ckeditor_uploader.fields
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(blank=True, max_length=150, null=True)),
                ('select_subjects', multiselectfield.db.fields.MultiSelectField(choices=[('Hindi', 'Hindi'), ('English', 'English'), ('Mathematics', 'Mathematics'), ('Science', 'Science'), ('Social_Studies', 'Social_Studies')], max_length=48)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(help_text='Please Enter Number or alphabet', max_length=50)),
            ],
        ),
    ]
