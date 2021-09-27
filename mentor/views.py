from django.shortcuts import render, get_object_or_404
from django.urls import reverse, resolve
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from mentor.form import *
from mentor.models import User
# Create your views here.


def index(request):
    return render(request, 'mentor/web.html')

 
def usersetup(request):

    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('nexus'))
                else:
                    return HttpResponse('User Not Active')
            else:
                print("Someone tried to login but failed")
                print("Username: {} \nPassword: {}".format(username, password))
                messages.warning(request, "Username or Password incorrect!")
                return HttpResponseRedirect(reverse('usersetup'))
        elif 'signup' in request.POST:
            UserForm = SignUpForm(data=request.POST)
            if UserForm.is_valid():
                user = UserForm.save()
                user.save()
            else:
                messages.error(request, UserForm.errors)
            return render(request, 'mentor/login.html', {'signup': UserForm})
    else:
        UserForm = SignUpForm()
        return render(request, 'mentor/login.html', {'signup': UserForm})


@login_required(login_url='usersetup')
def userprofile(request):
    profile = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        if 'mentor' in request.POST:
            mentor = MentorProfileForm(request.POST, request.FILES)
            if mentor.is_valid():
                mentor_user = mentor.save(commit=False)
                mentor_user.user = request.user
                if 'dop' in request.FILES:
                    mentor_user.dop = request.FILES['dop']
                    mentor_user.save()
                mentor_user.save()
                profile.registered = True
                profile.save()
                return HttpResponseRedirect(reverse('profile'))
            else:
                messages.error(request, mentor.errors)
        elif 'mentee' in request.POST:
            mentee = MenteeProfileForm(request.POST, request.FILES)
            if mentee.is_valid():
                mentee_user = mentee.save(commit=False)
                mentee_user.user = request.user
                if 'dop' in request.FILES:
                    mentee_user.dp = request.FILES['dop']
                    mentee_user.save()
                mentee_user.save()
                profile.registered = True
                profile.save()
                return HttpResponseRedirect(reverse('profile'))
            else:
                messages.error(request, mentee)
    else:
        mentorform = MentorProfileForm()
        menteeform = MenteeProfileForm()
    return render(request, 'mentor/stuProfile.html', {'profile': profile, 'mentorform': mentorform, 'menteeform':menteeform})


@login_required(login_url='usersetup')
def useroverview(request):
    profile = MenteeInfo.objects.get(user=request.user)
    return render(request, 'mentor/servicehome.html', {'user_active': profile})


@login_required(login_url='usersetup')
def suggestions(request):
    suggestions = MenteeInfo.objects.all()
    return render(request, 'mentor/serviceslibrary.html', {'suggestions': suggestions})


@login_required(login_url='usersetup')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home'))


@login_required(login_url='usersetup')
def follow_request(request, pk):
    following = get_object_or_404(MenteeInfo, pk=request.POST.get('follow'))
    follow = get_object_or_404(MenteeInfo, pk=pk)
    follow.following.add(following.user)
    following.followers.add(follow.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='usersetup')
def unfollow_request(request, pk):
    following = get_object_or_404(MenteeInfo, pk=request.POST.get('unfollow'))
    follow = get_object_or_404(MenteeInfo, pk=pk)
    follow.following.remove(following.user)
    following.followers.remove(follow.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='usersetup')
def accountupdate(request):
    user = MenteeInfo.objects.get(user=request.user)
    menteeform = MenteeProfileForm(instance=user)
    if request.method == 'POST':
        update = MenteeProfileForm(request.POST, request.FILES, instance=user)
        if update.is_valid():
            user_update = update.save(commit=False)
            if 'dop' in request.FILES:
                user_update.dp = request.FILES['dop']
                user_update.save()
            user_update.save()
            return HttpResponseRedirect(reverse('profile'))
    return render(request, 'mentor/accountupdate.html', {'menteeform': menteeform, 'user': user})


@login_required(login_url='usersetup')
def profileview(request, pk):
    profile = get_object_or_404(MenteeInfo, pk=pk)
    return render(request, 'mentor/profileview.html', {'profile': profile})

def post(request): 
    return render(request,"mentor/servicediscussion.html")

