from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView

from swapper import load_model

Notificacion = load_model('notify', 'Notification')


class NotificationList(ListView):
	model = Notificacion
	template_name = 'notificacion/notify.html'
	context_object_name = 'notify'


	@method_decorator(login_required)
	def dispatch(self, requets, *args, **kwargs):
		return super(NotificationList, self).dispatch(requets, *args, **kwargs)


	def get_queryset(self):
		return self.request.user.notificaciones.all()
