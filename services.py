from xml.etree import ElementTree
from collections import namedtuple

import requests

Episode = namedtuple('Episode', 'title link pubdate show_id')
episode_data = {}



def download_info():
    """
    Will download from rss talkpython

    :return: True if exists, False if doesn't exists
    """
    url = 'https://talkpython.fm/episodes/rss'

    # TODO: request data from url and show status
    res = requests.get(url)
    res.raise_for_status()

    # TODO: put response to html dom using ElementTree
    dom = ElementTree.fromstring(res.text)

    # TODO: find all items and count episode
    items = dom.findall('channel/item')
    episode_count = len(items)

    # TODO: loop item and put episode to dictionary
    for idx, item in enumerate(items):
        episode = Episode(
            item.find('title').text,
            item.find('link').text,
            item.find('pubDate').text,
            episode_count - idx - 1
        )
        episode_data[episode.show_id] = episode


# TODO: refers get_episode method to Episode tuple
def get_episode(show_id: int) -> Episode:
    return episode_data.get(show_id)

def get_latest_show_id():
    return max(episode_data.keys())