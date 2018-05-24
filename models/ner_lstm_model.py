#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
NER tagger for building a LSTM based NER tagging model.
"""

from bases.model_base import ModelBase


class NerLstmModel(ModelBase):
    """
    Ner for lstm model
    """

    def __init__(self, config):
        super(NerLstmModel, self).__init__(config)
        self.build_model()

    def build_model(self):
        main_input = Input(shape=(28 * 28,), name='main_input')
        x = Dense(units=32, activation='relu', kernel_initializer='random_uniform')(main_input)
        x = Dense(units=16, activation='relu')(x)
        output = Dense(units=10, activation='softmax')(x)
        model = Model([main_input], output)
        model.compile(loss='categorical_crossentropy',
                      optimizer=Adam(lr=self.config.lr),
                      metrics=['accuracy'])

        plot_model(model, to_file=os.path.join(self.config.img_dir, "model.png"), show_shapes=True)  # 绘制模型图

        self.model = model