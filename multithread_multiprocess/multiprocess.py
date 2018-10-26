#!/usr/bin/env python 
# coding:utf-8
# @Time :10/26/18 16:56

import time
from multithread_multiprocess import get_links, download_link, setup_download_dir
from multithread_multiprocess import logger
from multithread_multiprocess import CLIENT_ID
from functools import partial
from datetime import timedelta

from multiprocessing.pool import Pool


def main():
    ts = time.time()
    links = get_links(CLIENT_ID)
    logger.info("They has {} images".format(len(links)))
    download_dir = setup_download_dir()

    pool = Pool(4)
    download = partial(download_link, download_dir)

    with pool as p:
        p.map(download, links)

    logger.info("Took {} seconds".format(timedelta(seconds=time.time() - ts)))


if __name__ == '__main__':
    main()

