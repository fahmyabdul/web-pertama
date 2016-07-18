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
		return render(request, 'mainweb/adm_profil.html')
    else:
        return login_adm(request)

def adm_blog(request):
    if request.user.is_authenticated():
        posts = blog.models.Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
        users = User.objects.all()
        return render(request, 'mainweb/adm_blog.html', {'posts' : posts,'users' :users })
    else:
        return login_adm(request)

def adm_blog_user(request):
    if request.user.is_authenticated():
		return render(request, 'mainweb/adm_blog_user.html')
    else:
        return login_adm(request)
