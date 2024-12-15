from django.db import models

class Notification(models.Model):
    member_id = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return f"Notification for {self.member_id}"



