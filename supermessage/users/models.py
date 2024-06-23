from django.db import models


# Create your models here.
class Notification(models.Model):
    NOTIFICATION_OPTIONS = (
        ("email", "email"),
        ("push", "push"),
        ("no", "no"),
    )

    user = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    notification_option = models.CharField(max_length=5, choices=NOTIFICATION_OPTIONS, default="no")

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)
    
