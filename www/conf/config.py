#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Configuration
'''


import os

'''
Default configurations.
'''

PROJECTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 日志路径
LOG_DIR = os.path.join(PROJECTDIR,'logs/')

# 配置
configs = {
    'debug': True,
    'db': {
        'host': '112.74.89.67',
        'port': 3306,
        'user': 'zhihao',
        'password': 'zhihao',
        'db': 'zhihaoyu'
    },
    'session': {
        'secret': 'Awesome'
    }
}