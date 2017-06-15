#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' blog handlers '

import asyncio
import hashlib
import json
import logging
import re
import time

from aiohttp import web

import markdown2
from apis import Page, APIValueError, APIResourceNotFoundError
from conf.config import configs
from coroweb import get, post
from models import User, Comment, Blog, next_id
from common import utils

@get('/')
def index(*, page='1'):
    page_index = utils.get_page_index(page)
    num = yield from Blog.findNumber('count(id)')
    page = Page(num)
    if num == 0:
        blogs = []
    else:
        blogs = yield from Blog.findAll(orderBy='createDate desc', limit=(page.offset, page.limit))
    return {
        '__template__': 'blogs.html',
        'page': page,
        'blogs': blogs
    }

@get('/blog/{id}')
def get_blog(id):
    blog = yield from Blog.find(id)
    comments = yield from Comment.findAll('blog_id=?', [id], orderBy='createDate desc')
    for c in comments:
        c.html_content = utils.text2html(c.content)
    blog.html_content = markdown2.markdown(blog.content)
    return {
        '__template__': 'blog.html',
        'blog': blog,
        'comments': comments
    }
