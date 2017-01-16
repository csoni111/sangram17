from django.contrib import admin
from .models import College

# Register your models here.
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'college', 'city', 'email', 'mobile', 'mevents', 'fevents', 'status')
    actions = ['accept', 'reject', 'download_csv']
    def download_csv(self, request, queryset):
    	import csv
    	from django.http import HttpResponse
    	import StringIO
    	f = StringIO.StringIO()
    	writer = csv.writer(f)
    	writer.writerow(['Name', 'Designation', 'College', 'City', 'Email', 'Mobile', 'Male Events', 'Female Events', 'Status'])
    	for s in queryset:
        	writer.writerow([s.name, s.designation, s.college, s.city, s.email, s.mobile, s.mevents, s.fevents, s.status])
    	f.seek(0)
    	response = HttpResponse(f, content_type='text/csv')
    	response['Content-Disposition'] = 'attachment; filename=user_details.csv'
    	return response
    download_csv.short_description = "Download selected user details as CSV"

    def accept(self, request, queryset):
    	rows_updated = queryset.update(status=True)
    	if rows_updated == 1:
            message_bit = "1 college was"
        else:
            message_bit = "%s colleges were" % rows_updated
        self.message_user(request, "%s successfully accepted" % message_bit)
    accept.short_description = "Accept selected colleges"

    def reject(self, request, queryset):
    	rows_updated = queryset.update(status=False)
    	if rows_updated == 1:
            message_bit = "1 college was"
        else:
            message_bit = "%s colleges were" % rows_updated
        self.message_user(request, "%s successfully rejected" % message_bit)
    reject.short_description = "Reject selected colleges"

admin.site.register(College, CollegeAdmin)