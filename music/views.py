from multiprocessing import context
from django.shortcuts import render

from music.models import Music, About


def MusicListVeiw(request):
    music_list=Music.objects.all()

    context={
        'musiclist':music_list,
    }

    return render(request, 'music/music_list.html', context)


def AboutVeiw(request):
    ab=Music.objects.all()

    context={
        'about':ab,
    }

    return render(request, 'music/about.html', context)
    