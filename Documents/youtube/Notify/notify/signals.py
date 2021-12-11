# Django
from django.dispatch import Signal

notificar = Signal(providing_args= [
						'level',
						'destiny',
						'actor',
						'verbo',
						'timestamp'

					])