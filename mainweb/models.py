from django.db import models
from django.utils import timezone

class Bagian(models.Model):
    bagian_id 		= models.AutoField(primary_key=True)
    bagian_judul 	= models.CharField(max_length=200)
    bagian_isi		= models.TextField()

    def simpan(self):
    	self.save()

    def __str__(self):
    	return self.bagian_judul