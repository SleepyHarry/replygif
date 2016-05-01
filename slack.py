import os
import json
import requests


slack_url = 'https://slack.com/api/chat.postMessage'

if os.path.exists('.token'):
    token = open('.token').read().strip()
else if os.environ.get('SLACK_TOKEN'):
    token = os.environ['SLACK_TOKEN']
else:
    token = None


if os.path.exists('.sbim'):
   slackbot_im_channel_id = open('.sbim').read().strip()
else if os.environ.get('SLACKBOT_CHANNEL_ID.'):
   slackbot_im_channel_id = os.environ['SLACKBOT_CHANNEL_ID.']
else:
   slackbot_im_channel_id = None


def construct_message(image_url):
    return {
        'text': '',
        'attachments': [
            {
                'pretext': '',
                'image_url': image_url,
            }
        ]
    }


def post_image_message(image_url, channel_id, token):
    message = construct_message(image_url)

    message.update({
        'token': token,
        'channel': channel_id,
    })

    message['attachments'] = json.dumps(message['attachments'])

    return requests.post(slack_url, data=message)
