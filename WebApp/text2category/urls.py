from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'text2category'

urlpatterns = [
    url(r'^$', views.create, name="file_create"),
]

urlpatterns += staticfiles_urlpatterns()