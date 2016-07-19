from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Bagian
import blog

def main_view(request):
	bagians = Bagian.objects.all()
	return render(request, 'mainweb/main_view.html', {'bagians':bagians})

def login_adm(request):
    if request.user.is_authenticated():
        return redirect('/adm/profil')
    else:
        return login(request)

def adm_profil(request):
    if request.user.is_authenticated():
        alamat = request.path
        alamat = alamat.replace("/"," > ")
        alamats = alamat.replace(">", " ", 1)[:-2]
        return render(request, 'mainweb/adm_profil.html', {'alamats':alamats})
    else:
        return login_adm(request)

def adm_blog(request):
    if request.user.is_authenticated():
        alamat   = request.path
        alamat   = alamat.replace("/"," > ")
        alamats  = alamat.replace(">", " ", 1)[:-2]
        posts    = blog.models.Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
        totposts = posts.count()
        totpubs   = blog.models.Post.objects.filter(published_date__isnull=False).count()
        totunpubs = blog.models.Post.objects.filter(published_date__isnull=True).count()
        users    = User.objects.all()
        return render(request, 'mainweb/adm_blog.html', 
        {'posts' : posts, 'totposts': totposts, 'totpubs' : totpubs,
        'totunpubs' : totunpubs, 'users' :users,'alamats':alamats })
    else:
        return login_adm(request)

def adm_blog_user(request):
    if request.user.is_authenticated():
        alamat = request.path
        alamat = alamat.replace("/"," > ")
        alamats = alamat.replace(">", " ", 1)[:-2]
        return render(request, 'mainweb/adm_blog_user.html',{'alamats':alamats})
    else:
        return login_adm(request)
