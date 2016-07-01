from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bagian

def main_view(request):
	bagians = Bagian.objects.all()
	return render(request, 'mainweb/main_view.html', {'bagians':bagians})

def main_coba(request):
	return render(request, 'mainweb/main_coba.html')
