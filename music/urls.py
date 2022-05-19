from django.urls import path

from music import views


urlpatterns = [
    path('', views.MusicListVeiw),
    path('about', views.AboutVeiw),
    path('music/detail/<int:music_id>', views.MusicDetailView)
]
