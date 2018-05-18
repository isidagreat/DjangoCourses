from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^addcourse$', views.add),
	url(r'^courses/destroy/(?P<id>\d+)$', views.confirm),
	url(r'destroy$', views.destroy)
]