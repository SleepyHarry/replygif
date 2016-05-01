import json
import requests


slack_url = 'https://slack.com/api/chat.postMessage'


def post_image_message(image_url, channel_id, token):
    message = {
        'token': token,
        'channel': channel_id,
        'text': '',
        'attachments': json.dumps([
            {
                'pretext': '',
                'image_url': image_url,
            }
        ])
    }

    response = requests.post(slack_url, data=message)

    return response
