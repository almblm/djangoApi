from django.contrib import admin

# Register your models here.
from django.contrib import admin
from sample.models import SampleName

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','bookType')
    list_display_links = ('name','bookType')

admin.site.register(SampleName,BookAdmin)