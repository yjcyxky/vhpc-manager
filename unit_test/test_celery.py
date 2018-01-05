#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------------
#  Copyright (C) 2017 Nordata.
#  Website: nordata.com.cn
#
#  Swarm platform is developed by the Nordata company.
#  See the license for more details.
#  Author: Jingcheng Yang <yjcyxky@163.com>

from src.swarm.celery import debug_task
from src.ssadvisor.tasks import add

if __name__ == '__main__':
    import sys
    print(sys.path)
    print(debug_task.delay())
    print(add.delay(1, 2))
