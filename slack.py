import json

import requests
from django.conf import settings


def message(content, attachments=None):
    """
    curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/[HASH]/[HASH]/[HASH]

    :param content:
    :return:

    """

    headers = {
        'Content-type': 'application/json',
    }

    data = {
        "text": content,
    }

    if attachments:
        data.update({
            "attachments": attachments,
        })
    data = json.dumps(data)
    response = requests.post(
        settings.SLACK_HOOK, #your bot hook url
        headers=headers,
        data=data
    )
    return response