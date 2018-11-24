# -*- coding:utf-8 -*-

import configparser

__config = configparser.ConfigParser()
__config.read("credential.conf")

credential_section = "Credential"
url_key = 'url'
username_key = 'username'
password_key = 'password'
instance_id_key = 'instance_id'


def load_param_from_config(config, section, key):
    """
    :param section: str
    :param key: str
    :return: str
    """
    try:
        return config.get(section, key)
    except:
        return None


class CredentialInfo:
    def __init__(self, path_to_config='config/credential.conf'):
        self.__config = configparser.ConfigParser()
        self.__config.read(path_to_config)

        self.__URL = load_param_from_config(self.__config, credential_section, url_key)
        self.__USERNAME = load_param_from_config(self.__config, credential_section, username_key)
        self.__PASSWORD = load_param_from_config(self.__config, credential_section, password_key)
        self.__INSTANCE_ID = load_param_from_config(self.__config, credential_section, instance_id_key)

    @property
    def url(self):
        return self.__URL

    @property
    def username(self):
        return self.__USERNAME

    @property
    def password(self):
        return self.__PASSWORD

    @property
    def instance_id(self):
        return self.__INSTANCE_ID

    @property
    def info(self):
        wml_credentials = {
            "url": self.url,
            "username": self.username,
            "password": self.password,
            "instance_id": self.instance_id
        }
        return wml_credentials
