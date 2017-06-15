#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author zhihao.yu

import logging
import os
from logging.handlers import TimedRotatingFileHandler

from conf import config

def getLogger(name = None, level = logging.INFO, console_out = False):
    #logger = logging.getLogger("root")
    if isinstance(level, str):
        level = level.lower()
    if level == "debug":
        level = logging.DEBUG
    elif level == "info":
        level = logging.INFO
    elif level == "warning":
        level = logging.WARNING
    elif level == "error":
        level = logging.ERROR
    else:
        level = logging.DEBUG
    if name is None:
        name = 'root'

    if not os.path.exists(config.LOG_DIR):
        os.makedirs(config.LOG_DIR)
    LOG_FILE = config.LOG_DIR + "%s.log" % name

    fmt = "%(asctime)s - %(processName)s - %(filename)s[line:%(lineno)d] %(levelname)s - %(message)s"
    formatter = logging.Formatter(fmt)
    # TimedRotatingFileHandler 用自动处理log文件
    handler = TimedRotatingFileHandler(LOG_FILE, when='MIDNIGHT', interval=1, backupCount=10)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    if console_out == True:
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter(fmt)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    logger.setLevel(level)
    return logger




