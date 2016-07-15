from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$',views.main_view, name='main_view'),
	url(r'^adm/$', views.main_adm, name='adm_main'),
	url(r'^adm/profil/$', views.adm_profil, name='adm_profil'),
	url(r'^adm/blog/$', views.adm_blog, name='adm_blog'),
	url(r'^adm/blog/user/$', views.adm_blog_user, name='adm_blog'),
]