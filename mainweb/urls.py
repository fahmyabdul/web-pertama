from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$',views.main_view, name='main_view'),
	url(r'^coba/$', views.main_coba, name='main_coba'),
]