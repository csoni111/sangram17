from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    actions = ['download_csv']

    def download_csv(self, request, queryset):
    	import csv
    	from django.http import HttpResponse
    	import StringIO 

    	f = StringIO.StringIO()
    	writer = csv.writer(f)
    	writer.writerow(["code", "country", "ip", "url", "count"])
 
    	for s in queryset:
        	writer.writerow([s.code, s.country, s.ip, s.url, s.count])
 
    	f.seek(0)
    	response = HttpResponse(f, content_type='text/csv')
    	response['Content-Disposition'] = 'attachment; filename=user_details.csv'
    	return response

    download_csv.short_description = "Download selected user details as CSV"

admin.site.unregister(User)
admin.site.register(User, UserAdmin)