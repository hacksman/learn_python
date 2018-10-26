#!/usr/bin/env python 
# coding:utf-8
# @Time :10/26/18 19:27


from PIL import Image
from pathlib import Path

import time
from datetime import timedelta
from multithread_multiprocess import logger


def thumbnail_nail(size, path):
    image = Image.open(path)
    image.thumbnail(size)
    name = path.stem + "_thumbmail" + path.suffix
    thumbnail_path = path.with_name(name)
    image.save(thumbnail_path)


def main():
    ts = time.time()
    img_count = 0
    for img_path in Path("images").iterdir():
        img_count += 1
        thumbnail_nail((128, 128), img_path)
    logger.info("There has {} images".format(img_count))
    logger.info("Took {} seconds".format(timedelta(seconds=time.time()-ts)))


if __name__ == '__main__':
    main()