#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Copyright (c) 2018 by contributors. All Rights Reserved.
Author: Qichao Tang <qichaotang97@163.com>
base conf class
"""

import os

from .base_conf import BaseConf
from utility.log import WARNING_LOG


class NerBiLstmCrfConf(BaseConf):
    """
    ner bi-lstm-crf conf class
    """

    def __init__(self):
        # general config
        # TODO: 这些配置都可以放入配置文件中去
        self.dir_output = "results/test/"
        self.dir_model = self.dir_output + "model.weights/"
        self.path_log = self.dir_output + "log.txt"

        # embeddings
        self.dim_word = 300
        self.dim_char = 100

        # glove files
        self.filename_glove = "data/glove.6B/glove.6B.{}d.txt".format(self.dim_word)
        # self.trimmed embeddings (created from glove_filename with build_data.py)
        self.filename_trimmed = "data/glove.6B.{}d.trimmed.npz".format(self.dim_word)
        self.use_pretrained = True

        # dataset
        # self.filename_dev = "data/coNLL/eng/eng.testa.iob"
        # self.filename_test = "data/coNLL/eng/eng.testb.iob"
        # self.filename_train = "data/coNLL/eng/eng.train.iob"

        self.filename_train = "data/test.txt"
        self.filename_dev = "data/test.txt"
        self.filename_test = "data/test.txt"

        self.max_iter = None  # if not None, max number of examples in Dataset

        # vocab (created from dataset with build_data.py)
        self.filename_words = "data/words.txt"
        self.filename_tags = "data/tags.txt"
        self.filename_chars = "data/chars.txt"
        # vocabulary


        # training
        self.train_embeddings = False
        self.nepochs = 15
        self.dropout = 0.5
        self.batch_size = 20
        self.lr_method = "adam"
        self.lr = 0.001
        self.lr_decay = 0.9
        self.clip = -1  # if negative, no clipping
        self.nepoch_no_imprv = 3

        # model hyperparameters
        self.hidden_size_char = 100  # lstm on chars
        self.hidden_size_lstm = 300  # lstm on word embeddings

        # NOTE: if both chars and crf, only 1.6x slower on GPU
        self.use_crf = True  # if crf, training is 1.7x slower on CPU
        self.use_chars = True  # if char embedding, training is 3.5x slower on CPU

    def load(self, conf_filename):
        """
        load conf_filename init conf parameters
        :param conf_filename:
        :return:
        """

        # conf file exists
        if not os.path.isfile(conf_filename):
            WARNING_LOG("conf_filename:" + conf_filename + "not exists")
            return
