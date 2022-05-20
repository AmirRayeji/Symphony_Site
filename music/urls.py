from django.urls import path

from music import views


urlpatterns = [
    path('', views.MusicListVeiw),
    path('about', views.AboutVeiw),
    path('detail/<int:music_id>', views.MusicDetailView),
    path('gallery', views.GalleryVeiw),
]
