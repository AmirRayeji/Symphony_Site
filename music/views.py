from multiprocessing import context
from django.shortcuts import render

from music.models import Music, About, Gallery


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
    