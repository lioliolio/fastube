import os

from celery import Task

from notifications.models import SMSNotification
from .base import SendNotificationBaseTask


class SendSMSTask(SendNotificationBaseTask):

    def get_object(self, object_id):
        sms = SMSNotification.objects.get(pk=object_id)
        return sms

    def get_api_base_url(self):
        base_url = os.environ.get("SMS_API_BASE_URL")
        return base_url

    def get_headers(self):
        headers = {
            'x-waple-authorization': os.environ.get("SMS_API_HEADERS"),
        }
        return headers

    def get_data(self, object):
        data = {
            "send_phone": object.sender,
            "dest_phone": object.receiver,
            "msg_body": object.content,
        }
