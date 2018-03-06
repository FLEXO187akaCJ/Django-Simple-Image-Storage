from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.get_pictures_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.get_picture_comment, name='post_detail'),
	url(r'^post/new/$', views.upload_picture, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.edit_comment, name='post_edit'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)