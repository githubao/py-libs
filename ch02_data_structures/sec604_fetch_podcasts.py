#!/usr/bin/env python
# encoding: utf-8

"""
@description: 使用队列实现多线程下载

@author: baoqiang
@time: 2019/11/28 8:14 下午
"""
import json
from queue import Queue
import threading
import time
import urllib
from urllib.parse import urlparse
import feedparser

num_fetch_threads = 4
enclosure_queue = Queue()

feed_urls = [
    'https://talkpython.fm/episodes/rss'
]


def message(s):
    print('{}: {}'.format(threading.current_thread().name, s))


def download_enclosures(q):
    while True:
        message('looking for the next enclosure')

        url = q.get()

        filename = url.rpartition('/')[-1]
        message('downloading {}'.format(filename))

        # response = urllib.request.urlopen(url)
        # data = response.read()
        #
        # message('writing to {}'.format(filename))
        # with open(filename, 'wb') as fw:
        #     fw.write(data)

        q.task_done()


def run604_01():
    for url in feed_urls:
        response = feedparser.parse(url, agent='fetch_podcasts.py')

        for entry in response['entries'][:5]:
            for enclosure in entry.get('enclosures', []):
                parsed_url = urlparse(enclosure['url'])
                message('queuing {}'.format(
                    parsed_url.path.rpartition('/')[-1]))
                enclosure_queue.put(enclosure['url'])

    for i in range(num_fetch_threads):
        worker = threading.Thread(
            target=download_enclosures,
            args=(enclosure_queue,),
            name='worker-{}'.format(i),
        )

        worker.setDaemon(True)
        worker.start()

    message('*** main thread waiting')
    enclosure_queue.join()
    message('*** done')
