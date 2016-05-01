import requests
import json
import random


__all__ = [
    'all_tags',
    'get_urls',
    'random_gif',
]


# TODO: Multiple tags
tag_url_f = 'http://replygif.net/api/gifs?tag={tag}&api-key=39YAprx5Yi'.format


all_tags = [x.get('title') for x in
        json.loads(requests.get('http://replygif.net/api/tags?reaction=1&api-key=39YAprx5Yi').text)
    ]

def get_urls(tag):
    url = tag_url_f(tag=tag)

    response = requests.get(url)
    response.raise_for_status()

    j = json.loads(response.text)

    gif_urls = [x.get('file') for x in j]

    return gif_urls


def random_gif(tag=None):
    if tag is None:
        tag = random.choice(all_tags)

    all_gifs = get_urls(tag)

    return random.choice(all_gifs)
