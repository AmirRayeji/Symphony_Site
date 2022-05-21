from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from music.models import Music, About, Gallery
import account


def MusicListVeiw(request):
    music_list=Music.objects.all()

    context={
        'musiclist':music_list,
    }

    return render(request, 'music/music_list.html', context)


def AboutVeiw(request):
    ab=About.objects.all()

    context={
        'about':ab,
    }

    return render(request, 'music/about.html', context)


@login_required
def MusicDetailView(request, music_id):

        music=Music.objects.get(pk=music_id)

        context={
            'musicdetail':music
        }

        return render(request, 'music/music_detail.html', context)

def GalleryVeiw(request):
    gl=Gallery.objects.all()

    context={
        'gallery':gl,
    }

    return render(request, 'music/gallery.html', context)
    