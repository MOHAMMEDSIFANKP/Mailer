from django.contrib import admin
from .models import Mail
# Register your models here.


class MailAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'timestamp', )
admin.site.register(Mail,MailAdmin)