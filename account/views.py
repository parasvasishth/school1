from django.shortcuts import render , HttpResponse ,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import *
from .decorators import *
from .models import *
from employes.forms import *
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView as DefaultLogoutView, LoginView as DefaultLoginView
from django.shortcuts import render

from .forms import LoginForm



def dashboard(request):
    return render(request, 'account/adminlte/index.html')

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password('password')
            new_user.save()
            return HttpResponse('Done')
                # render(request,'student/create_student.html',{'new_user':new_user})
    else:
        user_form = RegisterForm()
    return render(request,'account/dashbord/form.html',{'user_form':user_form})


# def login(request):
#     return HttpResponse('hello from login')
#




def edit_media(request):
    if request.method == 'POST':

        input_form = MediaUploadForm(instance = request.user.MediaUpload,
                                    data=request.POST)
        if input_form.is_valid():
            input_form = input_form.save(commit = False)

            input_form.save()
    else:
        input_form = MediaUploadForm(instance = request.user.MediaUpload)

    return render(request,'account/upload_media.html',{'input_form':input_form})

@login_required
def basic_info(request):
    if request.method == 'POST':
        basic = SchoolProfileForm(instance = request.user.schoolprofile,
                                data = request.POST)
        if basic.is_valid():
            basic = basic.save(commit = False)
            basic.save()
    else:
        basic = SchoolProfileForm(instance = request.user.schoolprofile)
    return render(request,'account/profile.html',{'basic':basic})


def create_alert(request):
    if request.method == 'POST':
            form = Alert_form(request.POST,request.FILES or None)
            if form.is_valid():
                form.save()
            return HttpResponse('success')
    else:
        form = Alert_form()
    return render(request, 'account/adminlte/create_alert.html',{'form': form})


def alert_list(request):
    list = Alert.objects.all()
    return render(request,'account/dashbord/alert_list.html',{'alert':list})


def feeds(request):
    alert = Alert.objects.all()
    return render(request, 'account/dashbord/feeds.html',{'alert':alert})


def add_class(request):
    return render(request, 'account/dashbord/formadd_class.html',{})

from django.contrib.auth.views import LogoutView as DefaultLogoutView, LoginView as DefaultLoginView
from django.shortcuts import render

from .forms import LoginForm

from django.core.mail import send_mail
#
#
# def LoginView(request):
#     if request.method =='POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request,user)
#             return redirect('account:dashboard')
#     else:
#         form = LoginForm()
#         return render(request, 'account/login.html', {'form':form})

class LoginView(DefaultLoginView):
    authentication_form = LoginForm
    template_name = 'account/login.html'
    success_url = 'account:dashboard'




class LogoutView(DefaultLogoutView):
    success_url = '/'


def registerform(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('account:student:student_list')
    else:
        form = RegisterForm()
    return render(request, 'account/dashbord/form.html',{'s_form':form})

def academic_calender(request):
    if request.method == 'POST':
        form = AcademicCalenderForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponse('Done')
    else:
        form = AcademicCalenderForm()
    return render(request,'account/adminlte/calender.html',{'form':form})

def time_table(request):
    if request.method == 'POST':
        form = TimeTableForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('Done')
    else:
        form = TimeTableForm()
    return render(request,'account/adminlte/time_table.html',{'form':form})

def syllabus(request):
    if request.method == 'POST':
        form = SyllabusForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = SyllabusForm()
    return render(request,'account/adminlte/syllabus.html',{'form':form})

def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['vineet2603@gmail.com',]

    send_mail( subject, message, email_from, recipient_list )

    return render(request , 'account/email.html')





