#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Bi-LSTM-CRF data preprocess
"""

from .base_dict import BaseDict


class NerBiLstmCrfDict(BaseDict):
    def __init__(self, config=None):
        super(NerBiLstmCrfDict, self).__init__(config)

    def get_train_data(self):
        pass

    def get_test_data(self):
        pass