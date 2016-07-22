from django.conf.urls import include, url
import django.contrib.auth.views
from . import views

urlpatterns = [
	url(r'^$',views.main_view, name='main_view'),
	url(r'^adm/$', views.login_adm, name='login_adm'),
	url(r'^adm/profil/$', views.adm_profil, name='adm_profil'),
	url(r'^adm/blog/post/$', views.adm_blog_post, name='adm_blog_post'),
	url(r'^adm/blog/post/(?P<pk>\d+)/$', views.adm_blog_post_detail, name='adm_blog_post_detail'),
	url(r'^adm/blog/post/(?P<pk>\d+)/edit/$', views.adm_blog_post_edit, name='adm_blog_post_edit'),
	url(r'^adm/blog/user/$', views.adm_blog_user, name='adm_blog_user'),
    url(r'^adm/logout/$', views.logout_adm, name='logout_adm'),
]