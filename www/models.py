#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''


import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField, IntegerField, DateField
from common import utils

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'user'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    username = StringField(ddl='varchar(50)')
    password = StringField(ddl='varchar(50)')
    admin = BooleanField(default = True)
    nickname = StringField(ddl='varchar(50)')
    photopath = StringField(ddl='varchar(500)')
    registDate = DateField(default=utils.getDateStr())

class Blog(Model):
    __table__ = 'blog'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    title = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    createDate = DateField(default=utils.getDateStr())

class Comment(Model):
    __table__ = 'comment'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    createDate = DateField(default=utils.getDateStr())
