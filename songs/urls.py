from django.conf.urls import url

from . import views

urlpatterns = [
    #URL for ListView
    url(r'^$', views.SongListView.as_view(), name='list'),
    #URLs for CRUD Views
    url(r'^(?P<pk>\d+)/$', views.SongDetailView.as_view(), name='detail'),
    #CreateView does not require <pk> to be passed because it has not yet been created
    url(r'^create/$', views.SongCreateView.as_view(), name='create'),
    url(r'^edit/(?P<pk>\d+)/$', views.SongUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.SongDeleteView.as_view(), name='delete'),
]
