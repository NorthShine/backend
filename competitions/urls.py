from django.urls import path

from competitions import views


urlpatterns = [
    path('competency/', views.CreateCompetency.as_view()),
    path('competency/level/', views.CreateCompetitionLevel.as_view())
]
