import os
from configparser import ConfigParser

BasePath = os.path.dirname(__file__)
FilePath = os.path.join(BasePath, 'config.ini')


class ReadIni:
    def __init__(self):
        config = ConfigParser()
        config.read(FilePath)

        self.url = config.get('homepage', 'url')

        # 登录
        self.username = config.get('login_user', 'username')
        self.password = config.get('login_paw', 'password')
        self.sub = config.get('login_sub', 'sub')

        # 首页
        self.main = config.get('main_top', 'main')

        # 客户单位管理
        self.customer = config.get('customer', 'customer')
        self.customer_unit = config.get('customer_unit', 'customer_unit')
        self.customer_num = config.get('customer_opertion', 'customer_opertion_num')
        self.customer_frame = config.get('customer_opertion', 'customer_opertion_frame')

        # 新增
        self.customer_add = config.get('customer_opertion', 'customer_opertion_add')

        # 输入信息
        self.enter_message_frame = config.get('enter_message_add', 'enter_message_frame')
        self.enter_message_company = config.get('enter_message_add', 'enter_message_company')
        self.enter_message_type = config.get('enter_message_add', 'enter_message_type')
        self.enter_message_type2 = config.get('enter_message_add', 'enter_message_type2')
        self.enter_message_department = config.get('enter_message_add', 'enter_message_department')
        self.enter_message_site = config.get('enter_message_add', 'enter_message_site')
        self.enter_message_sub = config.get('enter_message_add', 'enter_message_sub')

        # 编辑
        self.customer_select = config.get('customer_opertion', 'customer_opertion_select')
        self.customer_editor = config.get('customer_opertion', 'customer_opertion_editor')

        # 输入信息
        self.enter_message_ed = config.get('enter_message_editor', 'enter_message_frame')
        self.enter_message_linkmen = config.get('enter_message_editor', 'enter_message_linkmen')
        self.enter_message_phone = config.get('enter_message_editor', 'enter_message_phone')

        # 删除
        self.customer_delete = config.get('customer_opertion', 'customer_opertion_delete')
        self.customer_delete_sure = config.get('customer_opertion', 'customer_opertion_delete_sure')

        # 搜索
        self.customer_search = config.get('customer_opertion', 'customer_opertion_search')
        self.customer_search_sub = config.get('customer_opertion', 'customer_opertion_search_sub')

        # 我的客户
        self.my_customer = config.get('my_customer', 'my_customer')
        self.my_customer_frame = config.get('my_customer', 'my_customer_frame')
        self.my_customer_num = config.get('my_customer', 'my_customer_num')
        self.my_customer_name = config.get('my_customer', 'my_customer_name')

        # 新增
        self.my_customer_add = config.get('my_customer', 'my_customer_add')

        # 输入框
        self.enter_add_message_frame = config.get('my_customer_add', 'enter_message_frame')
        self.enter_message_name = config.get('my_customer_add', 'enter_message_name')
        self.enter_message_unit = config.get('my_customer_add', 'enter_message_unit')
        self.enter_message_ubit_select = config.get('my_customer_add', 'enter_message_ubit_select')
        self.enter_message_phone = config.get('my_customer_add', 'enter_message_phone')
        self.enter_message_department = config.get('my_customer_add', 'enter_message_department')
        self.enter_message_department_select = config.get('my_customer_add', 'enter_message_department_select')
        self.enter_message_sub = config.get('my_customer_add', 'enter_message_sub')

        # 编辑
        self.my_customer_editor_select = config.get('my_customer', 'my_customer_editor_select')
        self.my_customer_editor = config.get('my_customer', 'my_customer_editor')

        # 输入框
        self.enter_editor_message_frame = config.get('my_customer_editor', 'enter_message_frame')
        self.enter_editor_message_name = config.get('my_customer_editor', 'enter_message_name')
        self.enter_message_WeChat = config.get('my_customer_editor', 'enter_message_WeChat')
        self.enter_message_Telephone = config.get('my_customer_editor', 'enter_message_Telephone')
        self.enter_message_hobby = config.get('my_customer_editor', 'enter_message_hobby')
        self.enter_message_address = config.get('my_customer_editor', 'enter_message_address')
        self.enter_message_sub = config.get('my_customer_editor', 'enter_message_sub')

        # 删除
        self.my_customer_delete_select = config.get('my_customer', 'my_customer_editor_select')
        self.my_customer_delete = config.get('my_customer', 'my_customer_delete')
        self.my_customer_delete_sub = config.get('my_customer_delete', 'my_customer_delete_sub')

        # 搜索
        self.my_customer_search = config.get('my_customer', 'my_customer_search')
        self.my_customer_search_sub = config.get('my_customer', 'my_customer_search_sub')


a = ReadIni()
print(a.customer_select)
print(a.customer_delete)
