#!/usr/bin/env python 
# coding:utf-8
# @Time :10/26/18 20:09

import asyncio
import aiohttp

import os
import time

from multithread_multiprocess import logger
from multithread_multiprocess import CLIENT_ID
from multithread_multiprocess import setup_download_dir
from multithread_multiprocess import get_links

from datetime import timedelta


async def async_download_link(session, directory, link):
    download_path = directory / os.path.basename(link)

    async with session.get(link) as response:
        with download_path.open("wb") as f:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                f.write(chunk)
    logger.info("Download {} image".format(link))


async def main():
    download_dir = setup_download_dir()
    async with aiohttp.ClientSession(conn_timeout=3, read_timeout=3) as session:
        links = get_links(CLIENT_ID)
        logger.info("There has {} images".format(links.__len__()))
        tasks = [(async_download_link(session, download_dir, l)) for l in links]
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    ts = time.time()

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
    logger.info("Took {} seconds".format(timedelta(seconds=time.time() - ts)))
