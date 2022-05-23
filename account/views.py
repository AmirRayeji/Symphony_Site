from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

import music


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