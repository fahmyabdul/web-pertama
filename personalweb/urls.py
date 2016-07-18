from django.conf.urls import include, url
import django.contrib.auth.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('mainweb.urls')),
    url(r'^blog/',include('blog.urls')),
]
