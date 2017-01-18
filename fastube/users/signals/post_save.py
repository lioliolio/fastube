import os
import json
import requests
from time import sleep

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=get_user_model())
def post_save_user(sender, instance, created, **kwargs):
    if created:
        sleep(3)
        slack_webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
        data = {
            "text": "{username} 님이 회원가입 했습니다.".format(username=instance.username),
            "username": "fastube",
            "icon_emoji": ":ghost:",
        }

        response = requests.post(
            slack_webhook_url,
            data=json.dumps(data),
        )
