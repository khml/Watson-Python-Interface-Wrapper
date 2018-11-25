# -*- coding:utf-8 -*-

from WPI import get_client


class Service:
    def __init__(self, client=None):
        if client is None:
            client = get_client()
        self.__service = client.service_instance

    @property
    def detail(self):
        return self.__service.get_details()

    @property
    def instance_id(self):
        return self.__service.get_instance_id()

    @property
    def password(self):
        return self.__service.get_password()

    @property
    def url(self):
        return self.__service.get_url()

    @property
    def username(self):
        return self.__service.get_username()
