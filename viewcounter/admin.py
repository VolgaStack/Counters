from django.contrib import admin

from .models import Counter, Summary, MetricaSettings

class CounterAdmin(admin.ModelAdmin):    
    list_display = ('counter', 'code_status', 'name', 'site', 'type')
    list_filter = ['site', 'type', 'code_status',]
    search_fields = ['name',]


class SummaryAdmin(admin.ModelAdmin):    
    list_display = ('name', 'start_date', 'end_date', 'visits', 'timestamp')
    search_fields = ['name',]
	
class MetricaSettingsAdmin(admin.ModelAdmin):    
    list_display = ('name', 'client_id', 'client_pass', 'token', )
    search_fields = ['name',]

admin.site.register(Counter, CounterAdmin)	
admin.site.register(Summary, SummaryAdmin)
admin.site.register(MetricaSettings, MetricaSettingsAdmin)