from django.db import models
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in

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
	log_action	= models.TextField()

	def simpan(self):
		self.save()

	def __str__(self):
		return self.log_authid