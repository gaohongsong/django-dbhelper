# -*- coding: utf-8 -*-
"""
    模块内参数配置，对外提供修改
"""
import os
from django.conf import settings

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

RUN_MODE = getattr(settings, 'RUN_MODE', 'DEVELOP')
