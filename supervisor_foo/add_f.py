

import time
import sys
import os

sys.path.append(".")
sys.path.append("../")
sys.path.append("../../..")

from python_log import logger


def main():
    i = 0
    while i < 15:
        i += 1
        time.sleep(1)
        logger.info("this is {} times".format(i))


if __name__ == '__main__':
    main()
