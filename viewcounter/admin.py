from django.contrib import admin

from .models import Counter, Summary

class CounterAdmin(admin.ModelAdmin):    
    list_display = ('counter_id', 'code_status', 'name', 'site', 'type')
    list_filter = ['site', 'type', 'code_status',]
    search_fields = ['name',]


class SummaryAdmin(admin.ModelAdmin):    
    list_display = ('counter_id', 'name', 'start_date', 'end_date', 'visits', 'timestamp')
    search_fields = ['name',]

admin.site.register(Counter, CounterAdmin)	
admin.site.register(Summary, SummaryAdmin)