#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from pye.models import Device
from django.shortcuts import render
from pye.forms import DeviceForm, EditDevice
from django.http import HttpResponseRedirect


def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        # 如果请求为POST,并且Form校验通过,把新添加的学员信息写入数据库
        if form.is_valid():
            s1 = Device(name=request.POST.get('name'),
                        ip_address=request.POST.get('ip_address'),
                        ro_community=request.POST.get('ro_community'),
                        rw_community=request.POST.get('rw_community'),
                        username=request.POST.get('username'),
                        password=request.POST.get('password'),
                        enable_password=request.POST.get('enable_password'),
                        device_type=request.POST.get('device_type'))
            s1.save()

            form = DeviceForm()
            return render(request, 'add_device.html', {'form': form,
                                                       'successmessage': '设备添加成功'})

        else:  # 如果Form校验失败,返回客户在Form中输入的内容和报错信息
            # 如果检查到错误,会添加错误内容到form内,例如:<ul class="errorlist"><li>IP地址已经存在</li></ul>
            return render(request, 'add_device.html', {'form': form})
    else:  # 如果不是POST,就是GET,表示为初始访问, 显示表单内容给客户
        form = DeviceForm()
        return render(request, 'add_device.html', {'form': form})


def show_device(request):
    # 查询整个数据库的信息 object.all()
    result = Device.objects.all()
    # 最终得到设备清单devices_list,清单内部是每一个设备信息的字典
    devices_list = []
    for x in result:
        # 产生学员信息的字典
        device_dict = {'id_delete': "/delete_device/" + str(x.id) + "/",
                       'id_edit': "/edit_device/" + str(x.id) + "/",
                       'id': x.id,
                       'name': x.name,
                       'ip_address': x.ip_address,
                       'ro_community': x.ro_community,
                       'rw_community': x.rw_community,
                       'username': x.username,
                       'password': x.password,
                       'enable_password': x.enable_password,
                       'device_type': x.device_type}

        # 提取学员详细信息,并写入字典
        devices_list.append(device_dict)
    return render(request, 'show_device.html', {'devices_list': devices_list})


def delete_device(request, id):
    # 获取对应ID的学员
    m = Device.objects.get(id=id)
    # 从数据库中删除学员条目
    m.delete()
    # 成功后重定向到显示所有学员信息页面
    return HttpResponseRedirect('/show_device')


def getdeviceinfo(device_id):
    result = Device.objects.get(id=device_id)
    device_dict = {'id': result.id,
                   'name': result.name,
                   'ip_address': result.ip_address,
                   'ro_community': result.ro_community,
                   'rw_community': result.rw_community,
                   'username': result.username,
                   'password': result.password,
                   'enable_password': result.enable_password,
                   'device_type': result.device_type}
    return device_dict


def edit_device(request, id):
    if request.method == 'POST':
        form = EditDevice(request.POST)
        # 如果请求为POST,并且Form校验通过,把新添加的学员信息写入数据库
        if form.is_valid():
            d = Device.objects.get(id=id)
            d.name = request.POST.get('name')
            d.ip_address = request.POST.get('ip_address')
            d.ro_community = request.POST.get('ro_community')
            d.rw_community = request.POST.get('rw_community')
            d.username = request.POST.get('username')
            d.password = request.POST.get('password')
            d.enable_password = request.POST.get('enable_password')
            d.device_type = request.POST.get('device_type')
            d.save()

            return HttpResponseRedirect('/show_device')

        else:  # 如果Form校验失败,返回客户在Form中输入的内容和报错信息
            # 如果检查到错误,会添加错误内容到form内,例如:<ul class="errorlist"><li>IP地址已经存在</li></ul>
            return render(request, 'edit_device.html', {'form': form})
    else:  # 如果不是POST,就是GET,表示为初始访问, 显示表单内容给客户
        device_dict = getdeviceinfo(id)
        form = EditDevice(initial={'id': device_dict.get('id'),
                                   'name': device_dict.get('name'),
                                   'ip_address': device_dict.get('ip_address'),
                                   'ro_community': device_dict.get('ro_community'),
                                   'rw_community': device_dict.get('rw_community'),
                                   'username': device_dict.get('username'),
                                   'password': device_dict.get('password'),
                                   'enable_password': device_dict.get('enable_password'),
                                   'device_type': device_dict.get('device_type'),
                                   })
        return render(request, 'edit_device.html', {'form': form})

