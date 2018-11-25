# -*- coding:utf-8 -*-

from WPI import get_client


class Repository:
    def __init__(self, client=None):
        if client is None:
            client = get_client()
        self.__repository = client.repository

    @property
    def list(self):
        return self.__repository.list()

    @property
    def detail(self):
        return self.__repository.list()


