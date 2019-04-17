#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from django.shortcuts import render


def index_def(request):
    return render(request, 'index.html', {'qytangtitle': '强化班作业title',
                                          'qytangbody': '强化班作业body'})

