#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from django.shortcuts import render
from datetime import datetime
from data import courses_db
from qytdb.models import Courses
import json
from django.contrib.auth.decorators import login_required


def summary_def(request):
    # mytime = int(datetime.now().strftime("%w"))
    mytime = int(datetime.strptime('2019-04-14', '%Y-%m-%d').strftime("%w"))
    qytsummary_title = 'QYT課程摘要Title'
    qytsummary = 'QYT課程摘要Body'
    # courses_list = ['安全', 'Python', 'DC']
    courses_list = []
    teacher_list = []
    courses_result = Courses.objects.all()
    for x in courses_result:
        courses_list.append(x.courses_name)
        teacher_list.append({'courses': x.courses_name, 'teacher': x.courses_teacher})

    # teacher_list = [{'courses': '安全', 'teacher': '现任明教教主'},
    #                 {'courses': '数据中心', 'teacher': '马海波'},
    #                 {'courses': '路由交换', 'teacher': '安德'},
    #                 {'courses': '教主VIP', 'teacher': '现任明教教主'},
    #                 ]

    return render(request, 'summary.html', locals())


@login_required()
def sec_course(request):
    c = Courses.objects.get(courses_name='安全')
    courses_sec = {'方向': c.courses_name,
                   '摘要': c.courses_summary,
                   '授课老师': c.courses_teacher,
                   '授课方式': c.courses_method,
                   '课程特色': c.courses_characteristic,
                   '试验环境': c.courses_provide_lab,
                   '具体课程': json.loads(c.courses_detail)}
    return render(request, 'course.html', {'courseinfo': courses_sec})


@login_required()
def dc_course(request):
    c = Courses.objects.get(courses_name='数据中心')
    courses_dc = {'方向': c.courses_name,
                  '摘要': c.courses_summary,
                  '授课老师': c.courses_teacher,
                  '授课方式': c.courses_method,
                  '课程特色': c.courses_characteristic,
                  '试验环境': c.courses_provide_lab,
                  '具体课程': json.loads(c.courses_detail)}
    return render(request, 'course.html', {'courseinfo': courses_dc})
