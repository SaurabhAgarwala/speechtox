from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'playlistcategorize'

urlpatterns = [
    url(r'^$', views.playlist_categorize, name="playlist_categorize"),
]

urlpatterns += staticfiles_urlpatterns()