#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

_ROOT = os.path.abspath(os.path.dirname(__file__))
_ROOT = os.path.abspath(os.path.join(_ROOT, '..'))


def get_data(dpath):
    return os.path.join(_ROOT, 'data', dpath)


def get_model(mpath):
    return os.path.join(_ROOT, 'model', mpath)


def get_human(hpath):
    return os.path.join(_ROOT, 'human', hpath)


def get_mouse(upath):
    return os.path.join(_ROOT, 'mouse', upath)
