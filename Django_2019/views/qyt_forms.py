from qytdb.models import StudentsDB
from django.http import HttpResponseRedirect
from django.shortcuts import render
from qytdb.forms import StudentsForm
from qytdb.forms import StudentsForm,EditStudents
from django.contrib.auth.decorators import permission_required


@permission_required('qytdb.add_studentsdb')
def addstudent(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        # 如果请求为POST,并且Form校验通过,把新添加的学员信息写入数据库
        if form.is_valid():
            s1 = StudentsDB(name=request.POST.get('name'),
                            phone_number=request.POST.get('phone_number'),
                            qq_number=request.POST.get('qq_number'),
                            mail=request.POST.get('mail'),
                            direction=request.POST.get('direction'),
                            class_adviser=request.POST.get('class_adviser'),
                            payed=request.POST.get('payed'))
            s1.save()
            # 写入成功后,重定向返回展示所有学员信息的页面
            return HttpResponseRedirect('/showstudents')
        else:  # 如果Form校验失败,返回客户在Form中输入的内容和报错信息
            # 如果检查到错误,会添加错误内容到form内,例如:<ul class="errorlist"><li>QQ号码已经存在</li></ul>
            return render(request, 'addstudent.html', {'form': form})
    else:  # 如果不是POST,就是GET,表示为初始访问, 显示表单内容给客户
        form = StudentsForm()
        return render(request, 'addstudent.html', {'form': form})


@permission_required('qytdb.view_studentsdb')
def showstudents(request):
    # 查询整个数据库的信息 object.all()
    result = StudentsDB.objects.all()
    # 最终得到学员清单students_list,清单内部是每一个学员信息的字典
    students_list = []
    for x in result:
        # 产生学员信息的字典
        students_dict = {}
        # 为了不在模板中拼接字符串,提前为删除和编辑页面产生URI
        students_dict['id_delete'] = "/deletestudent/" + str(x.id) + "/"
        students_dict['id_edit'] = "/editstudent/" + str(x.id) + "/"

        # 提取学员详细信息,并写入字典
        students_dict['id'] = x.id
        students_dict['name'] = x.name
        students_dict['phone_number'] = x.phone_number
        students_dict['qq_number'] = x.qq_number
        students_dict['mail'] = x.mail
        students_dict['direction'] = x.direction
        students_dict['class_adviser'] = x.class_adviser
        students_dict['payed'] = x.payed
        students_dict['date'] = x.date
        students_list.append(students_dict)
    return render(request, 'showstudents.html', {'students_list': students_list})


@permission_required('qytdb.delete_studentsdb')
def deletestudent(request, id):
    # 获取对应ID的学员
    m = StudentsDB.objects.get(id=id)
    # 从数据库中删除学员条目
    m.delete()
    # 成功后重定向到显示所有学员信息页面
    return HttpResponseRedirect('/showstudents')


def getstudentinfo(id):
    # 设置过滤条件,获取特定学员信息, objects.get(id=id)
    result = StudentsDB.objects.get(id=id)
    students_dict = {}
    students_dict['id'] = result .id
    students_dict['name'] = result .name
    students_dict['phone_number'] = result .phone_number
    students_dict['qq_number'] = result .qq_number
    students_dict['mail'] = result .mail
    students_dict['direction'] = result .direction
    students_dict['class_adviser'] = result .class_adviser
    students_dict['payed'] = result .payed
    students_dict['date'] = result .date
    # 返回特定学员详细信息
    return students_dict


@permission_required('qytdb.change_studentsdb')
def editstudent(request, id):
    # 首先获取特定ID学员详细信息
    infodict = getstudentinfo(id)
    if request.method == 'POST':
        form = EditStudents(request.POST)
        # 如果请求为POST,并且Form校验通过,把修改过的学员信息写入数据库
        if form.is_valid():
            m = StudentsDB.objects.get(id=id)
            m.name = request.POST.get('name')
            m.phone_number = request.POST.get('phone_number')
            m.qq_number = request.POST.get('qq_number')
            m.mail = request.POST.get('mail')
            m.direction = request.POST.get('direction')
            m.class_adviser = request.POST.get('class_adviser')
            m.payed = request.POST.get('payed')
            m.save()
            # 写入成功后,重定向返回展示所有学员信息的页面
            return HttpResponseRedirect('/showstudents')
        else:  # 如果Form校验失败,返回客户在Form中输入的内容和报错信息
            return render(request, 'editstudent.html', {'form': form})
    else:  # 如果不是POST,就是GET,表示为初始访问, 把特定ID客户在数据库中的值,通过初始值的方式展现给客户看
        form = EditStudents(initial={'id': infodict['id'], # initial填写初始值
                                     'name': infodict['name'],
                                     'phone_number': infodict['phone_number'],
                                     'qq_number': infodict['qq_number'],
                                     'mail': infodict['mail'],
                                     'direction': infodict['direction'],
                                     'class_adviser': infodict['class_adviser'],
                                     'payed': infodict['payed']})
        return render(request, 'editstudent.html', {'form': form})
