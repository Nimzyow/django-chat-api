from django.contrib import admin
from users.models import Notification


# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Notification, NotificationAdmin)