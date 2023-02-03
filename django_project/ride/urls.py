from django.urls import path
from .views import (
    RideOwnerListView, 
    RideOwnerDetailView,
    RideOwnerCreateView,
    RideOwnerUpdateView,
    RideOwnerDeleteView
)
from . import views

#app_name = 'polls'
urlpatterns = [
    # ex: /
    #path('', views.home, name='ride-home'),
    path('', RideOwnerListView.as_view(), name='ride-home'),

    path('ride/<int:pk>/', RideOwnerDetailView.as_view(), name='ride-detail'),
    path('ride/new/', RideOwnerCreateView.as_view(), name='ride-create'),
    path('ride/<int:pk>/update/', RideOwnerUpdateView.as_view(), name='ride-update'),
    path('ride/<int:pk>/delete/', RideOwnerDeleteView.as_view(), name='ride-delete'),
    # ex: /about/
    path('about/', views.about, name='ride-about'),
    #path('rideowner/', RideListView.as_view(), )



    # # ex: /polls/
    # path('', views.IndexView.as_view(), name='index'),
    # # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]