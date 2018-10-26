#!/usr/bin/env python 
# coding:utf-8
# @Time :10/26/18 18:03

import time
from multithread_multiprocess import get_links, download_link, setup_download_dir
from multithread_multiprocess import logger
from multithread_multiprocess import CLIENT_ID
from functools import partial
from datetime import timedelta

from concurrent.futures import ThreadPoolExecutor


def main():
    ts = time.time()

    download_dir = setup_download_dir()
    links = get_links(CLIENT_ID)
    logger.info("There has {} images".format(links.__len__()))

    with ThreadPoolExecutor(max_workers=20) as exectutor:
        download = partial(download_link, download_dir)
        exectutor.map(download, links, timeout=30)
    logger.info("Took {} seconds".format(timedelta(seconds=time.time() - ts)))


if __name__ == '__main__':
    main()
