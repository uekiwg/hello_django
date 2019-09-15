from django.urls import path

from .views import *

app_name = 'polls'
urlpatterns = [
    path('', index.IndexView.as_view(), name='index'),
    path('<int:pk>/', detail.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', result.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote.VoteView.as_view(), name='vote'),
    # # ex: /polls/
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
