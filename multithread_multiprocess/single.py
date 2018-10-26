#!/usr/bin/env python 
# coding:utf-8
# @Time :10/26/18 14:19

import time
from multithread_multiprocess import setup_download_dir
from multithread_multiprocess import download_link
from multithread_multiprocess import get_links
from multithread_multiprocess import CLIENT_ID

from multithread_multiprocess import logger
from datetime import timedelta


def main():

    ts = time.time()
    download_dir = setup_download_dir()
    links = get_links(CLIENT_ID)
    logger.info("They has {} images".format(len(links)))

    for link in links:
        download_link(download_dir, link)

    # worker
    logger.info("Took {} seconds".format(timedelta(seconds=time.time() - ts)))


if __name__ == '__main__':
    main()
