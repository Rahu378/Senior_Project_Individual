from django.shortcuts import render
from .models import Notification

def list_notifications(request, member_id):
    notifications = Notification.objects.filter(member_id=member_id)
    if not notifications.exists():
        return render(request, 'notifications/not_found.html', {'member_id': member_id})
    return render(request, 'notifications/notifications_list.html', {
        'member_id': member_id,
        'notifications': notifications
    })
