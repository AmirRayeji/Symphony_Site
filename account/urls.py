from django.urls import path

from account import views


urlpatterns = [
    path('login/', views.LoginView),
    path('logout/', views.LogoutView),
    path('profile', views.ProfileView)
]
