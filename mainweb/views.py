from django.shortcuts import render, get_object_or_404, redirect
from .models import Bagian

def main_view(request):
	bagians = Bagian.objects.all()
	return render(request, 'mainweb/main_view.html', {'bagians':bagians})
