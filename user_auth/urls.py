from django.urls import path

from user_auth import views


urlpatterns = [
    path('profiles/', views.ListProfiles.as_view()),
    path('profiles/<str:email>/', views.ListProfile.as_view()),
    path('register/', views.CreateUser.as_view())
]
