from django.conf.urls import include, url
import django.contrib.auth.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/accounts/login/$', django.contrib.auth.views.login, name='login'),
    url(r'^blog/accounts/logout/$', django.contrib.auth.views.logout, name='logout', kwargs={'next_page': '/blog/'}),
    url(r'',include('mainweb.urls')),
    url(r'^blog/',include('blog.urls')),
]
