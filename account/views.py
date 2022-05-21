from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
import music


def LoginView(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse(music.views.MusicListVeiw))
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