# -*- coding: utf-8 -*-

# -----------------------------------------------------------
#  Copyright (C) 2017 Nordata.
#  Website: nordata.com.cn
#
#  Swarm platform is developed by the Nordata company.
#  See the license for more details.
#  Author: Jingcheng Yang <yjcyxky@163.com>

from __future__ import unicode_literals

from django.apps import AppConfig
import platform

class SscobwebConfig(AppConfig):
    name = "sscobweb"
    settings = {
        'ROOT_PREFIX': '/opt/local/cobweb',
        'SYSTEM': 'Linux',
        'ARCH': 'x86_64'
    }
