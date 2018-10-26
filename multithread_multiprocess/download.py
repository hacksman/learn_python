#!/usr/bin/env python 
# coding:utf-8
# @Time :10/26/18 11:19

import json
import logging
import requests
import os
from pathlib import Path
from urllib.request import urlopen, Request
from multithread_multiprocess import CLIENT_ID


logger = logging.getLogger(__name__)

types = {'image/jpeg', 'image/png'}


def get_links(client_id):
    headers = {'Authorization': 'Client-ID {}'.format(client_id)}
    req = requests.get('https://api.imgur.com/3/gallery/random/random/', headers=headers)
    req_json = req.json()
    items = []
    for per_data in req_json.get("data"):
        if 'type' in per_data and per_data['type'] in types:
            items.append(per_data['link'])
    return items


def download_link(directory, link):
    download_path = directory / os.path.basename(link)
    with urlopen(link) as image, download_path.open('wb') as f:
        f.write(image.read())
    logger.info('Downloaded %s', link)


def setup_download_dir():
    download_dir = Path('images')
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir


if __name__ == '__main__':
    print(get_links(CLIENT_ID))
    # print(os.path.basename('https://i.imgur.com/PRMwhty.jpg'))
    # print(setup_download_dir())