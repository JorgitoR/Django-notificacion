
#Django
from django.contrib import admin


class AbstractNotifyAdmin(admin.ModelAdmin):
	raw_id_fields = ('destiny',)
	list_dysplay = ('destiny', 'actor', 'verbo', 'read', 'publico')
	list_filter = ('level', 'read')

	def get_queryset(self, requets):
		qs = super(AbstractNotifyAdmin, self).get_queryset(requets)
		return qs.prefetch_related('actor')