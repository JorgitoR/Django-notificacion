from django import template 

register = template.Library()

@register.filter()
def notificaciones(context):

	user = user_context(context)

	if not user:
		return ''

	return user.notificaciones.no_leido().count()

notificaciones = register.simple_tag(takes_context=True)(notificaciones)

def user_context(context):

	if 'user' not in context:
		return None 

	request = context['request']
	user = request.user  

	try:

		user_is_anonymous = user.is_anonymous()
	except TypeError:
		user_is_anonymous = user.is_anonymous

	if user_is_anonymous:
		return None 

	return user