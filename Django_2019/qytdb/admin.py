from django.contrib import admin
from qytdb.models import StudentsDB
from qytdb.models import Courses
# Register your models here.

# 可以在管理界面使用户为staff,就可以登录管理页面
# 为用户设置的权限,在管理界面依然会限制用户操作数据库的权限


# 下面的命令register,Pycharm识别不了,只能直接敲
admin.site.register(StudentsDB)
admin.site.register(Courses)
