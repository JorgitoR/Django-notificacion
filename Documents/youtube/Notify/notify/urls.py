from django.urls import path

from .views import NotificationList

urlpatterns = [

	path('notify/', NotificationList.as_view(), name='notify')
]