from django.contrib import admin
from django.conf.urls import url, include
# from text2category import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^text2category/', include('text2category.urls')),
    url(r'^songcategory/', include('songcategory.urls')),
    url(r'^playlistcategorize/', include('playlistcategorize.urls')),
    url(r'^$', views.home, name="home"),
    url(r'^team/$', views.team, name="team"),
]

urlpatterns += staticfiles_urlpatterns()