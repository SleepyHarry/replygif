import json

import gif
import slack

from flask import Flask, jsonify, request, abort


app = Flask(__name__)


@app.route('/')
def test():
    return 'Hello, World!'


@app.route('/gif/', methods=['GET', 'POST'])
def main():
    data = request.form

    token = data.get('token')
    if token != slack.expected_token:
        abort(403, 'got invalid token: {}'.format(token))

    tag = data.get('text')

    if tag == '--help' or tag == '-h':
        return jsonify({
            'text': 'possible tags:\n\t' + '\n\t'.join(gif.all_tags),
        })

    gif_url = gif.random_gif(tag)

    message_data = slack.construct_message(gif_url)
    message_data.update({
        'as_user': True,
    })

    source_channel_id = data.get('channel_id')
    source_channel_name = data.get('channel_name')

    response = slack.post_image_message(message_data, source_channel_id)
    response_data = json.loads(response.text)

    if not response_data['ok']:
        return '', 400

    return '', 200


if __name__ == '__main__':
    app.run(debug=True)
