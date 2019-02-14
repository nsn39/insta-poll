from django.urls import path
from polls import views as polls_views

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('specifics/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('about_me/' ,views.AboutMeView.as_view(), name='about_me'),
    path('signup/', views.SignUp.as_view(), name='register'),
]

