from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'songcategory'

urlpatterns = [
    url(r'^$', views.categorize, name="song_categorize"),
]

urlpatterns += staticfiles_urlpatterns()