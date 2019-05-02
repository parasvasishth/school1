# Generated by Django 2.2 on 2019-05-01 09:33

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=15, unique=True)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], max_length=10)),
                ('date_of_birth', models.DateField(max_length=8)),
                ('subject_expertise', multiselectfield.db.fields.MultiSelectField(choices=[('english', 'ENGLISH'), ('hindi', 'HINDI'), ('maths', 'MATHS'), ('science', 'SCIENCE'), ('social science', 'SOCIAL_SCIENCE')], max_length=42)),
                ('experience', models.PositiveSmallIntegerField()),
                ('joining_date', models.DateField(max_length=8)),
                ('email_id', models.EmailField(max_length=254)),
                ('highest_qualification', models.CharField(max_length=20)),
            ],
        ),
    ]
