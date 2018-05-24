#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Copyright (c) 2018 by contributors. All Rights Reserved.
Author: Qichao Tang <qichaotang97@163.com>
log file
"""

import sys
import time


def get_time():
    """
    get_time
    """
    return str(time.strftime('%Y-%m-%d %X', time.localtime()))


def FATAL_LOG(log_str):
    """
    WARNING_LOG
    """
    sys.stderr.write("[FATAL][" + get_time() + "]\t" + str(log_str) + "\n")


def WARNING_LOG(log_str):
    """
    WARNING_LOG
    """
    sys.stderr.write("[WARNING][" + get_time() + "]\t" + str(log_str) + "\n")


def NOTICE_LOG(log_str):
    """
    NOTICE_LOG
    """
    sys.stderr.write("[NOTICE][" + get_time() + "]\t" + str(log_str) + "\n")


def TRACE_LOG(log_str):
    """
    TRACE_LOG
    """
    sys.stderr.write("[TRACE][" + get_time() + "]\t" + str(log_str) + "\n")


def DEBUG_LOG(log_str):
    """
    DEBUG_LOG
    """
    sys.stderr.write("[DEBUG][" + get_time() + "]\t" + str(log_str) + "\n")
