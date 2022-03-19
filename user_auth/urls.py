from django.urls import path

from user_auth import views


urlpatterns = [
    path('profiles/<str:email>/', views.ListProfile.as_view())
]
