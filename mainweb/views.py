from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Bagian

def main_view(request):
	bagians = Bagian.objects.all()
	return render(request, 'mainweb/main_view.html', {'bagians':bagians})

def main_adm(request):
	return render(request, 'mainweb/main_adm.html')

def adm_profil(request):
	return render(request, 'mainweb/adm_profil.html')

def adm_blog(request):
	return render(request, 'mainweb/adm_blog.html')

def adm_blog_user(request):
	return render(request, 'mainweb/adm_blog_user.html')
