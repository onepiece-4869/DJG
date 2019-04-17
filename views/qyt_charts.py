from django.shortcuts import render
from random import randint
from django.http import JsonResponse


def monitor_device(request):
        return render(request, 'monitor_device.html')


# 提供chart刷新的JSON数据
def chart_json(request, chart_type, deviceid):
    if chart_type == 'line' or chart_type == 'bar':
        colors = ['#007bff', '#28a745', '#333333', '#c3e6cb', '#dc3545', '#6c757d']
        labels = ['2019-4-1', '2019-4-2', '2019-4-3', '2019-4-4', '2019-4-5', '2019-4-6']
        datas = [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]
        return JsonResponse({'colors': colors, 'labels': labels, 'datas': datas})
    elif chart_type == 'pie':
        colors = ['#007bff', '#28a745', '#333333', '#c3e6cb', '#dc3545', '#6c757d']
        labels = ['安全', '数据中心', '教主VIP', '路由交换', '无线', '华为']
        datas = [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]
        return JsonResponse({'colors': colors, 'labels': labels, 'datas': datas})