import os
import json
import requests


slack_url = 'https://slack.com/api/chat.postMessage'

if os.path.exists('.token'):
    chat_token = open('.token').read().strip()
elif os.environ.get('SLACK_TOKEN'):
    chat_token = os.environ['SLACK_TOKEN']
else:
    chat_token = None


if os.path.exists('.sbim'):
   slackbot_im_channel_id = open('.sbim').read().strip()
elif os.environ.get('SLACKBOT_CHANNEL_ID.'):
   slackbot_im_channel_id = os.environ['SLACKBOT_CHANNEL_ID.']
else:
   slackbot_im_channel_id = None


expected_token = os.environ.get('EXPECTED_TOKEN')


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


def post_image_message(image_url, channel_id):
    message = construct_message(image_url)

    message.update({
        'token': chat_token,
        'channel': channel_id,
    })

    message['attachments'] = json.dumps(message['attachments'])

    return requests.post(slack_url, data=message)
