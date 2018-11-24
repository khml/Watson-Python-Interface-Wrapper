# -*- coding:utf-8 -*-

from config import CredentialInfo

from watson_machine_learning_client import WatsonMachineLearningAPIClient


def get_client(credential=None):
    if credential is None:
        credential = CredentialInfo()

    client = WatsonMachineLearningAPIClient(credential.info)
    return client
