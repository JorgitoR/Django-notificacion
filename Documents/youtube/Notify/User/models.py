from django.contrib.auth.models import AbstractUser


#Utils
from django.utils import timezone

# built-in signals
from django.db.models.signals import post_save

# signals
from notify.signals import notificar

# Django
from django.db import models

class Usuario(AbstractUser):
	lector =  models.BooleanField(default=True)



class Post(models.Model):
	user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	image = models.FileField(upload_to='fotos')
	text = models.TextField()
	timestamp = models.DateTimeField(default=timezone.now, db_index=True)

	def __str__(self):
		return self.title


def notify_post(sender, instance, created, **kwargs):

	notificar.send(instance.user, destiny=instance.user,  verb=instance.title, level='success')

post_save.connect(notify_post, sender=Post)

