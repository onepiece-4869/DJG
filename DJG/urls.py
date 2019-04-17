"""DJG URL Configuration

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
from views import index, qyt_forms, qyt_charts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.index_def),
    path('add_device', qyt_forms.add_device),
    path('show_device', qyt_forms.show_device),
    path('delete_device/<int:id>/', qyt_forms.delete_device),
    path('edit_device/<int:id>/', qyt_forms.edit_device),
    path('monitor_device', qyt_charts.monitor_device),
    path('monitor_device/<str:chart_type>/<int:deviceid>/', qyt_charts.chart_json),
]
