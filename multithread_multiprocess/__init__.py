#!/usr/bin/env python 
# coding:utf-8
# @Time :10/26/18 11:18

import logging

CLIENT_ID = "your_client_id"

from multithread_multiprocess.download import setup_download_dir
from multithread_multiprocess.download import download_link
from multithread_multiprocess.download import get_links

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

