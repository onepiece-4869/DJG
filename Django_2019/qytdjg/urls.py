"""qytdjg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from views import index, qytsummary, qyt_forms, qyt_charts, qyt_rpc, qyt_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.index_def),
    path('summary', qytsummary.summary_def),
    path('sec', qytsummary.sec_course),
    path('dc', qytsummary.dc_course),
    path('addstudent', qyt_forms.addstudent),
    path('showstudents', qyt_forms.showstudents),
    path('deletestudent/<int:id>/', qyt_forms.deletestudent),
    path('editstudent/<int:id>/', qyt_forms.editstudent),
    path('chartsjson/', qyt_charts.chartsjson),
    # 推荐的JSON刷新数据方式,提供JSON数据的页面
    path('chartjson/<str:chart_type>/<int:deviceid>/', qyt_rpc.chart_json),
    # 登录页面
    path('accounts/login/', qyt_login.qyt_login),
    # 注销页面
    path('accounts/logout/', qyt_login.qyt_logout),

]
