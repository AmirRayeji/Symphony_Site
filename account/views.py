from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from account.models import Profile
from account.forms import SignupForm, ProfileEditForm, UserEditForm
import music
import account


def LoginView(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))

            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        else:
            context={
                'username':username,
                'messageerror':'کاربری با این مشخصات یافت نشد!'
            }
            return render(request, 'account/login.html', context)
    else:
        return render(request, 'account/login.html', {})


def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse(music.views.MusicListVeiw))


@login_required
def ProfileView(request):
    profile=request.user.profile

    context={
        'profile':profile
    }

    return render(request, 'account/profile.html', context)

def SignupView(request):

    if request.method=="POST":
        signupform=SignupForm(request.POST,request.FILES)
        if signupform.is_valid():

            user=User.objects.create_user(username=signupform.cleaned_data['username'],
                                email=signupform.cleaned_data['email'],
                                password=signupform.cleaned_data['password'],
                                first_name=signupform.cleaned_data['first_name'],
                                last_name=signupform.cleaned_data['last_name'])

            user.save()

            ProfileModel=Profile(user=user,
                                       profile=signupform.cleaned_data['profile'],
                                        gender=signupform.cleaned_data['gender'])

            ProfileModel.save()

            return HttpResponseRedirect(reverse(music.views.MusicListVeiw))
    else:
        signupform=SignupForm()

  
    context={
        "formData":signupform
    }

    return render(request,"account/signup.html",context)

def ProfileEditView(request):

    if request.method=="POST":
        profileEditForm=ProfileEditForm(request.POST,request.FILES, instance=request.user.profile)
        userEditForm=UserEditForm(request.POST,instance=request.user)

        if profileEditForm.is_valid:
            profileEditForm.save()
            userEditForm.save()
            return HttpResponseRedirect(reverse(account.views.ProfileView))
    else:
        profileEditForm=ProfileEditForm(instance=request.user.profile)
        userEditForm=UserEditForm(instance=request.user)

    context={

        "profileEditForm":profileEditForm,
        "profile":request.user.profile.profile,
        "userEditForm":userEditForm
    }

    return render(request,"account/profileEdit.html",context)
