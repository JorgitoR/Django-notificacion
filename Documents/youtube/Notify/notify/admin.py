from django.contrib import admin

# Django
from notify.utils.admin import AbstractNotifyAdmin

# Models
from .models import Notification


admin.site.register(Notification, AbstractNotifyAdmin)