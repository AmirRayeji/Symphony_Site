from multiprocessing import context
from django.shortcuts import render

from music.models import Music


def MusicListVeiw(request):
    music_list=Music.objects.all()

    context={
        'musiclist':music_list
    }

    return render(request, 'music/music_list.html', context)
