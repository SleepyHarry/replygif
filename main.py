import gif
import slack

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def test():
    return 'Hello, World!'


@app.route('/gif/', methods=['GET', 'POST'])
def main():
    data = request.form

    tag = data.get('text')

    gif_url = gif.random_gif(tag)

    message_data = slack.construct_message(gif_url)

    return jsonify(message_data)


if __name__ == '__main__':
    app.run(debug=True)


#gif_url = gif.random_gif('thumbs up')
#gif_url = gif.random_gif()
#
#response = slack.post_image_message(gif_url, slackbot_im_channel_id, token)
#response.raise_for_status()
