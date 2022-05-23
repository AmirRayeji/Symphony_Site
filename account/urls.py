from django.urls import path

from account import views


urlpatterns = [
    path('login/', views.LoginView),
    path('logout/', views.LogoutView),
    path('profile/', views.ProfileView),
    path('signup/', views.SignupView),
    path('profileEdit/', views.ProfileEditView)
]
