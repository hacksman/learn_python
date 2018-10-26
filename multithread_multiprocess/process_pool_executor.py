#!/usr/bin/env python 
# coding:utf-8
# @Time :10/26/18 19:50

from multithread_multiprocess import logger
# from multithread_multiprocess import

import time
from datetime import timedelta
from PIL import Image
from pathlib import Path

from concurrent.futures import ProcessPoolExecutor
from functools import partial


def thumbnail_nail(size, path):
    image = Image.open(path)
    image.thumbnail(size)
    name = path.stem + "_thumbmail" + path.suffix
    thumbnail_path = path.with_name(name)
    image.save(thumbnail_path)


def main():
    ts = time.time()
    thumbnail_nail_size = partial(thumbnail_nail, (128, 128))
    with ProcessPoolExecutor() as executor:
        executor.map(thumbnail_nail_size, Path("images").iterdir())

    logger.info("Took {} seconds".format(timedelta(seconds=time.time() - ts)))


if __name__ == '__main__':
    main()
