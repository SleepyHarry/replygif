import gif
import slack


token = open('.token').read().strip()
slackbot_im_channel_id = open('.sbim').read().strip()


#gif_url = gif.random_gif('thumbs up')
gif_url = gif.random_gif()

response = slack.post_image_message(gif_url, slackbot_im_channel_id, token)
response.raise_for_status()
