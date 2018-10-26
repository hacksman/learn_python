#!/usr/bin/env python 
# coding:utf-8
# @Time :10/26/18 15:34

import time

from multithread_multiprocess import CLIENT_ID
from datetime import timedelta

from queue import Queue
from threading import Thread

from multithread_multiprocess import setup_download_dir, get_links, download_link
from multithread_multiprocess import logger


class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            download_dir, link = self.queue.get()
            try:
                download_link(download_dir, link)
            finally:
                self.queue.task_done()


def main():

    ts = time.time()
    download_dir = setup_download_dir()
    links = get_links(CLIENT_ID)
    logger.info("They has {} images".format(len(links)))

    queue = Queue()

    # worker
    for x in range(8):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()

    # producer
    for link in links:
        logger.info('Queueing {}'.format(link))
        queue.put((download_dir, link))

    queue.join()

    logger.info("Took {} seconds".format(timedelta(seconds=time.time() - ts)))


if __name__ == '__main__':
    main()
