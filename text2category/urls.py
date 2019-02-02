from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'text2category'

urlpatterns = [
    url(r'^$', views.create, name="file_create"),
    # url(r'^loggedin_create$', views.login_create, name="post_login_create"),
    # url(r'^(?P<url>[\w-]+)/$', views.paste_disp, name="disp"),
    # url(r'^loggedin/(?P<url>[\w-]+)/$', views.login_paste_disp, name="login_disp"),
    # url(r'^edit/(?P<id>[\w-]+)/$', views.edit, name="edit"),
    # url(r'^delete/(?P<id>[\w-]+)/$', views.delete, name="delete"),
]

urlpatterns += staticfiles_urlpatterns()