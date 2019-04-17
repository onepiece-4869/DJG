from django import forms
from django.core.validators import RegexValidator
from pye.models import Device


class DeviceForm(forms.Form):
    # 为了添加必选项前面的星号
    # 下面是模板内的内容
    """
    < style type = "text/css" >
    label.required::before
    {
        content: "*";
    color: red;
    }
    < / style >
    """
    required_css_class = 'required'  # 这是Form.required_css_class属性, use to add class attributes to required rows
    # 添加效果如下
    # <label class="required" for="id_name">设备名称:</label>
    # 不添加效果如下
    # <label for="id_name">设备名称:</label>

    # 设备名称,最小长度2,最大长度50,
    # label后面填写的内容,在表单中显示为名字,
    # 必选(required=True其实是默认值)
    # attrs={"class": "form-control"} 主要作用是style it in Bootstrap
    name = forms.CharField(max_length=50,
                           min_length=2,
                           label='设备名称',
                           required=True,
                           widget=forms.TextInput(attrs={"class": "form-control"}))
    # IP地址
    ip_address = forms.GenericIPAddressField(label='IP地址',
                                             required=True,
                                             widget=forms.TextInput(attrs={"class": "form-control"}))
    # 只读Community
    ro_community = forms.CharField(max_length=50,
                                   min_length=2,
                                   label='只读Community',
                                   required=True,
                                   widget=forms.TextInput(attrs={"class": "form-control"}))

    # 读写Community
    rw_community = forms.CharField(max_length=50,
                                   min_length=2,
                                   label='读写Community',
                                   required=False,
                                   widget=forms.TextInput(attrs={"class": "form-control"}))

    # SSH用户名
    username = forms.CharField(max_length=50,
                               min_length=2,
                               label='SSH用户名',
                               required=False,
                               widget=forms.TextInput(attrs={"class": "form-control"}))

    # SSH密码
    password = forms.CharField(max_length=50,
                               min_length=2,
                               label='SSH密码',
                               required=False,
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))

    # enable密码
    enable_password = forms.CharField(max_length=50,
                                      min_length=2,
                                      label='Enable密码',
                                      required=False,
                                      widget=forms.PasswordInput(attrs={"class": "form-control"}))

    # 设备类型
    device_type_choices = (('ASA', 'ASA'), ('Router', 'Router'), ('Switch', 'Switch'))
    device_type = forms.CharField(max_length=10,
                                  label='设备类型',
                                  widget=forms.Select(choices=device_type_choices, attrs={"class": "form-control"}))

    def clean_ip_address(self):  # 对IP地址的唯一性进行校验,注意格式为clean+校验变量
        ip_address = self.cleaned_data['ip_address']  # 提取客户输入的电话号码
        # 在数据库中查找是否存在这个IP地址
        existing = Device.objects.filter(ip_address=ip_address).exists()
        # 如果存在就显示校验错误信息
        if existing:
            raise forms.ValidationError("IP地址已经存在")
        # 如果校验成功就返回电话号码
        return ip_address

    def clean_password(self):
        password = self.cleaned_data['password']
        username = self.cleaned_data['username']
        if not (password and username):
            raise forms.ValidationError("用户名和密码需要同时填写")
        return password


class EditDevice(forms.Form):
    # 为了添加必选项前面的星号
    # 下面是模板内的内容
    """
    < style type = "text/css" >
    label.required::before
    {
        content: "*";
    color: red;
    }
    < / style >
    """
    required_css_class = 'required'  # 这是Form.required_css_class属性, use to add class attributes to required rows
    # 添加效果如下
    # <label class="required" for="id_name">设备名称:</label>
    # 不添加效果如下
    # <label for="id_name">设备名称:</label>

    # 设备名称,最小长度2,最大长度50,
    # label后面填写的内容,在表单中显示为名字,
    # 必选(required=True其实是默认值)
    # attrs={"class": "form-control"} 主要作用是style it in Bootstrap
    id = forms.CharField(label='设备唯一ID',
                         widget=forms.TextInput(attrs={"class": "form-control", 'readonly': True}))
    name = forms.CharField(max_length=50,
                           label='设备名称',
                           min_length=2,
                           required=True,
                           widget=forms.TextInput(attrs={"class": "form-control"}))
    # IP地址
    ip_address = forms.GenericIPAddressField(
        label='IP地址',
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    # 只读Community
    ro_community = forms.CharField(max_length=50,
                                   min_length=2,
                                   label='只读Community',
                                   required=True,
                                   widget=forms.TextInput(attrs={"class": "form-control"}))

    # 读写Community
    rw_community = forms.CharField(max_length=50,
                                   min_length=2,
                                   label='读写Community',
                                   required=False,
                                   widget=forms.TextInput(attrs={"class": "form-control"}))

    # SSH用户名
    username = forms.CharField(max_length=50,
                               min_length=2,
                               label='SSH用户名',
                               required=False,
                               widget=forms.TextInput(attrs={"class": "form-control"}))

    # SSH密码
    password = forms.CharField(max_length=50,
                               min_length=2,
                               label='SSH密码',
                               required=False,
                               widget=forms.TextInput(attrs={"class": "form-control"}))

    # enable密码
    enable_password = forms.CharField(max_length=50,
                                      min_length=2,
                                      label='Enable密码',
                                      required=False,
                                      widget=forms.TextInput(attrs={"class": "form-control"}))

    # 设备类型
    device_type_choices = (('ASA', 'ASA'), ('Router', 'Router'), ('Switch', 'Switch'))
    device_type = forms.CharField(max_length=10,
                                  label='设备类型',
                                  widget=forms.Select(choices=device_type_choices, attrs={"class": "form-control"}))

    def clean_ip_address(self):  # 对IP地址的唯一性进行校验,注意格式为clean+校验变量
        ip_address = self.cleaned_data['ip_address']  # 提取客户输入的电话号码
        # 在数据库中查找是否存在这个IP地址
        existing = Device.objects.filter(ip_address=ip_address).exists()
        # 如果存在就显示校验错误信息
        if existing:
            raise forms.ValidationError("IP地址已经存在")
        # 如果校验成功就返回电话号码
        return ip_address

    def clean_password(self):
        password = self.cleaned_data['password']
        username = self.cleaned_data['username']
        if not (password and username):
            raise forms.ValidationError("用户名和密码需要同时填写")
        return password
