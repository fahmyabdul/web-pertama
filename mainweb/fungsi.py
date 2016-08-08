from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib import messages
from .models import Login_log
import blog

class Totalposting():
    def totposts(request):
        posts_list  = blog.models.Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
        totposts    = posts_list.count()
        return totposts
    def totpubs(request):
        totpubs     = blog.models.Post.objects.filter(published_date__isnull=False).count()
        return totpubs
    def totunpubs(request):
        totunpubs   = blog.models.Post.objects.filter(published_date__isnull=True).count()
        return totunpubs

def halaman(request,obyek,jml_isi):
    paginator   = Paginator(obyek,jml_isi)
    page        = request.GET.get('page')
    try:
        isi = paginator.page(page)
    except PageNotAnInteger:
        isi = paginator.page(1)
    except EmptyPage:
        isi = paginator.page(paginator.num_pages)
    return isi

def entrilog(sender, request, user, **kwargs):
	if request.user.is_staff :
		messages.info(request, "Login berhasil dilakukan, selamat datang di administrator Tuan Abdul!")
	userid = request.user.id
	login_log = Login_log()
	login_log.log_authid 	= userid
	login_log.log_date 		= timezone.now()
	login_log.log_status	= 1
	login_log.log_session 	= request.session.session_key
	login_log.save()

def dellog(sender, request, user, **kwargs):
	if request.user.is_staff :
		messages.info(request, "Logout berhasil dilakukan.")
	userid = request.user.id
	login_log = Login_log.objects.filter(log_authid=userid)
	login_log.delete()

user_logged_in.connect(entrilog)
user_logged_out.connect(dellog)