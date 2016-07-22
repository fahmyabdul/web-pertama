from django.db import models
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.sessions.models import Session
from django.contrib import messages

class Bagian(models.Model):
    bagian_id 		= models.AutoField(primary_key=True)
    bagian_judul 	= models.CharField(max_length=200)
    bagian_isi		= models.TextField()

    def simpan(self):
    	self.save()

    def __str__(self):
    	return self.bagian_judul

class Profil(models.Model):
	profil_id		= models.AutoField(primary_key=True)
	profil_nama		= models.CharField(max_length=50)
	profil_alias	= models.CharField(max_length=50)
	profil_alamat	= models.TextField()
	profil_tlp		= models.IntegerField()

	def simpan(self):
		self.save()

	def __str__(self):
		return self.profil_nama

class Login_log(models.Model):
	log_id		= models.AutoField(primary_key=True)
	log_authid	= models.IntegerField()
	log_date	= models.DateTimeField(default=timezone.now)
	log_status	= models.IntegerField()
	log_session	= models.TextField(blank=True, null=True)

	def simpan(self):
		self.save()

	def __str__(self):
		return self.log_authid

def entrilog(sender, request, user, **kwargs):
	messages.info(request, "Login berhasil dilakukan, selamat datang di administrator Tuan Abdul!")
	userid = request.user.id
	login_log = Login_log()
	login_log.log_authid 	= userid
	login_log.log_date 		= timezone.now()
	login_log.log_status	= 1
	login_log.log_session 	= request.session.session_key
	login_log.save()

def dellog(sender, request, user, **kwargs):
	messages.info(request, "Logout berhasil dilakukan.")
	userid = request.user.id
	login_log = Login_log.objects.filter(log_authid=userid)
	login_log.delete()

user_logged_in.connect(entrilog)
user_logged_out.connect(dellog)