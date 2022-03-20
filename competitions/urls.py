from django.urls import path

from competitions import views


urlpatterns = [
    path('competency/', views.CreateCompetency.as_view()),
    path('competency/level/', views.CreateCompetitionLevel.as_view()),
    path('skilltoken/', views.SkillTokenView.as_view()),
    path('skilltoken/<int:id', views.SkillTokenView.as_view()),
    path('skilltoken/<str:email>/', views.SkillTokenView.as_view()),
    path('search/', views.SkillTokenSearchView.as_view())
]
