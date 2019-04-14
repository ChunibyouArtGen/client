from .client import run_client

import logging
from threading import Thread

logger = logging.getLogger()

def start_client():
    t = Thread(target=run_client, name='celestiaprime')
    t.start()


if __name__ == "__main__":
    start_client()