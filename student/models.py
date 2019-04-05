from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class StudentProfile(models.Model):

  student = models.OneToOneField(User,on_delete = models.CASCADE, related_name = 'studentprofile')
  student_name = models.CharField(max_length = 20, null = True , blank = True)
  student_class = models.PositiveIntegerField( null = True , blank = True)
  student_section = models.CharField(max_length = 5, null = True , blank = True)
  student_roll_number = models.CharField(max_length = 10, null = True , blank = True)
  father_name = models.CharField(max_length = 20, null = True , blank = True)
  mother_name = models.CharField(max_length = 20, null = True , blank = True)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '8885559997'. Up to 12 digits allowed along with country code.")
  guardian_mobile_number = models.CharField(validators=[phone_regex], max_length=12, blank=True)