import json
import requests


slack_url = 'https://slack.com/api/chat.postMessage'

token = open('.token').read().strip()
slackbot_im_channel_id = open('.sbim').read().strip()


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
