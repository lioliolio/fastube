import os
import json
import requests
from time import sleep

from celery import Task


class SimpleTask(Task):

    def run(self):
        sleep(3)
        slack_webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
        data = {
            "text": "회원가입 했습니다.",
            "username": "fastube",
            "icon_emoji": ":ghost:",
        }

        response = requests.post(
            slack_webhook_url,
            data=json.dumps(data),
        )
