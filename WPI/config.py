# -*- coding:utf-8 -*-

import os
import configparser

__DIRNAME_OF_THIS_FILE = os.path.dirname(__file__)

# Credential Info
__DEFAULT_CREDENTIAL_CONFIG_FILENAME = 'config/credential.conf'
default_credential_config = os.path.join(__DIRNAME_OF_THIS_FILE, __DEFAULT_CREDENTIAL_CONFIG_FILENAME)
CREDENTIAL_SECTION = "Credential"
URL_KEY = 'url'
USERNAME_PASSWORD = 'username'
PASSWORD_KEY = 'password'
INSTANCE_ID = 'instance_id'


def load_param_from_config(config, section, key):
    """
    :param config: configparser.ConfigParser
    :param section: str
    :param key: str
    :return:
    """
    try:
        return config.get(section, key)
    except:
        return None


class Info:
    def __init__(self, path_to_config):
        """
        :param path_to_config:
        """
        self.__config = configparser.ConfigParser()
        self.__config.read(path_to_config)

    def load_param_from_config(self, section, key):
        return load_param_from_config(self.__config, section, key)


class CredentialInfo(Info):
    def __init__(self, path_to_config=None):
        path_to_config = default_credential_config if path_to_config is None else path_to_config
        super().__init__(path_to_config)

        self.__URL = self.load_param_from_config(CREDENTIAL_SECTION, URL_KEY)
        self.__USERNAME = self.load_param_from_config(CREDENTIAL_SECTION, USERNAME_PASSWORD)
        self.__PASSWORD = self.load_param_from_config(CREDENTIAL_SECTION, PASSWORD_KEY)
        self.__INSTANCE_ID = self.load_param_from_config(CREDENTIAL_SECTION, INSTANCE_ID)

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
