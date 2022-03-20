from django.urls import path

from notifications import views


urlpatterns = [
    path('notification/<str:recipient_id>/', views.RedisNotification.as_view()),
    path('notification/', views.RedisNotification.as_view()),
    path('notification/persistent/', views.PersistentNotificationView.as_view()),
    path(
        'notification/persistent/<str:recipient_id>',
        views.PersistentNotificationView.as_view())
]
