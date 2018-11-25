# -*- coding:utf-8 -*-

from WPI.config import CredentialInfo

from watson_machine_learning_client import WatsonMachineLearningAPIClient


def get_client(wml_credentials=None):
    """
    wml_credentials is dict that:
        wml_credentials = {
            "url": str,
            "username": str,
            "password": str,
            "instance_id": str
        }

    if wml_credentials of arg is None, use default config info.

    :param wml_credentials: CredentialInfo or dict
    :return: WatsonMachineLearningAPIClient
    """
    if wml_credentials is None:
        wml_credentials = CredentialInfo().info

    client = WatsonMachineLearningAPIClient(wml_credentials)
    return client
