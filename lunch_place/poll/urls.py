from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_vote_choices),

    path('start/', views.start_poll),
    path('vote/', views.vote),
    path('end/', views.end_poll),
]
