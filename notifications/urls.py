from django.urls import path

from notifications import views


urlpatterns = [
    path('notification/<str:recipient_id>/', views.RedisNotification.as_view()),
    path('notification/', views.RedisNotification.as_view())
]
