#!/usr/bin/env python
# encoding: utf-8

"""
@description: 队列

@author: baoqiang
@time: 2019/11/28 8:01 下午
"""

import queue
import threading
import functools


def run601_01():
    q = queue.Queue()

    for i in range(5):
        q.put(i)

    while not q.empty():
        print(q.get(), end=' ')

    print()


def run601_02():
    """
    last in, first out
    :return:
    """
    q = queue.LifoQueue()

    for i in range(5):
        q.put(i)

    while not q.empty():
        print(q.get(), end=' ')

    print()


def run601_03():
    """
    priority queue
    NOTICE: ！！！优先级最低的先出队列！！！
    :return:
    """

    class Job:
        def __init__(self, priority, desc):
            self.priority = priority
            self.desc = desc
            print('new job:', desc)

        def __eq__(self, other):
            return self.priority == other.priority

        def __lt__(self, other):
            return self.priority < other.priority

    q = queue.PriorityQueue()

    q.put(Job(3, "Mid-level Job"))
    q.put(Job(10, "Low-level Job"))
    q.put(Job(1, "Important-level Job"))

    workers = [
        threading.Thread(target=process_job, args=(q,)),
        threading.Thread(target=process_job, args=(q,)),
    ]

    for w in workers:
        w.setDaemon(True)
        w.start()

    q.join()


def process_job(q):
    while True:
        next_job = q.get()
        print('Processing Job:', next_job.desc)
        q.task_done()
