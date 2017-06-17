#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' comment handlers '

import asyncio
import hashlib
import json
import logging
import re
import time

from aiohttp import web

import markdown2
from apis import Page, APIValueError, APIResourceNotFoundError, APIPermissionError
from conf.config import configs
from coroweb import get, post
from models import User, Comment, Blog, next_id
from common import utils,auth_utils


@post('/api/comments/{id}/delete')
def api_delete_comments(id, request):
    auth_utils.check_admin(request)
    c = yield from Comment.find(id)
    if c is None:
        raise APIResourceNotFoundError('Comment')
    yield from c.remove()
    return dict(id=id)


@get('/api/comments')
def api_comments(*, page='1'):
    page_index = utils.get_page_index(page)
    num = yield from Comment.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, comments=())
    comments = yield from Comment.findAll(orderBy='createDate desc', limit=(p.offset, p.limit))
    return dict(page=p, comments=comments)

@post('/api/blogs/{id}/comments')
def api_create_comment(id, request, *, content):
    user = request.__user__
    if user is None:
        raise APIPermissionError('Please signin first.')
    if not content or not content.strip():
        raise APIValueError('content')
    blog = yield from Blog.find(id)
    if blog is None:
        raise APIResourceNotFoundError('Blog')
    comment = Comment(blog_id=blog.id, user_id=user.id, user_name=user.username, user_image=user.photopath, content=content.strip())
    yield from comment.save()
    return comment


