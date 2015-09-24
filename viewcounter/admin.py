from django.contrib import admin

from .models import CountersInfo

class CountersInfoAdmin(admin.ModelAdmin):    
    list_display = ('period', 'counter_id', 'name', 'site', 'views', 'status', 'timestamp')
    list_filter = ['name', 'site']
    search_fields = ['status']
	
admin.site.register(CountersInfo, CountersInfoAdmin)
