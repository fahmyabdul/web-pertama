from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login,logout
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Bagian
import blog

def main_view(request):
	bagians = Bagian.objects.all()
	return render(request, 'mainweb/main_view.html', {'bagians':bagians})

def login_adm(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return redirect('/adm/blog')
        else:
            stat = 'bukanadmin'
            logout(request)
            return render(request, 'registration/login.html', {'stat':stat})
    else:
        return login(request)

def logout_adm(request):
    logout(request)
    return redirect('/adm/')


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
        alamat      = request.path
        alamat      = alamat.replace("/"," > ")
        alamats     = alamat.replace(">", " ", 1)[:-2]
        posts_list  = blog.models.Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
        totposts    = posts_list.count()
        totpubs     = blog.models.Post.objects.filter(published_date__isnull=False).count()
        totunpubs   = blog.models.Post.objects.filter(published_date__isnull=True).count()
        users       = User.objects.all()
        paginator   = Paginator(posts_list,10)
        page        = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
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
