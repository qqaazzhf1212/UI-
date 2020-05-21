from selenium import webdriver
from time import sleep
from util.readConfig import ReadIni as R
from util.readYaml import yaml_data as Y


class CMS:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = R().url
        self.driver.get(self.url)
        sleep(2)

    def id_element(self, id):
        return self.driver.find_element_by_id(id)

    def name_element(self, name):
        return self.driver.find_element_by_name(name)

    def classname_element(self, classname):
        return self.driver.find_element_by_class_name(classname)

    def xpath_element(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def css_element(self, css):
        return self.driver.find_element_by_css_selector(css)

    # 启动浏览器并输入数据登录
    def login(self, username, password):
        self.id_element(R().username).send_keys(username)
        self.id_element(R().password).send_keys(password)
        self.classname_element(R().sub).click()
        sleep(2)

    def main(self):
        self.xpath_element(R().main).click()
        sleep(2)

    def customer(self):
        self.xpath_element(R().customer).click()
        sleep(2)

    def customer_unit(self):
        self.xpath_element(R().customer_unit).click()
        sleep(2)

    # 客户信息流程
    def customer_flow(self):
        self.main()
        self.customer()
        self.customer_unit()
        sleep(5)

    # 获取客户信息数量
    def customer_num(self):
        self.driver.switch_to.frame(R().customer_frame)
        num = self.xpath_element(R().customer_num).text
        self.driver.switch_to.default_content()
        return num[1:3].strip()

    # 客户单位增加
    def customer_opertion_add(self):
        # 新增
        self.driver.switch_to.frame(R().customer_frame)
        self.xpath_element(R().customer_add).click()
        sleep(2)
        self.driver.switch_to.default_content()

        # 输入信息
        self.driver.switch_to.frame(R().enter_message_frame)
        self.xpath_element(R().enter_message_company).send_keys('武汉市汉阳分局')
        sleep(2)
        self.xpath_element(R().enter_message_type).click()
        sleep(2)
        self.xpath_element(R().enter_message_type2).click()
        sleep(2)
        self.xpath_element(R().enter_message_department).send_keys('部门')
        sleep(2)
        self.xpath_element(R().enter_message_site).send_keys('武汉市汉阳区')
        sleep(2)
        self.xpath_element(R().enter_message_sub).click()
        self.xpath_element(R().enter_message_sub).click()
        self.driver.switch_to.default_content()
        sleep(5)

    # 编辑
    def customer_opertion_editor(self):
        # 进入编辑
        self.driver.switch_to.frame(R().customer_frame)
        self.xpath_element(R().customer_select).click()
        self.xpath_element(R().customer_editor).click()
        self.driver.switch_to.default_content()
        sleep(5)

        # 编辑框
        self.driver.switch_to.frame(R().enter_message_ed)
        self.xpath_element(R().enter_message_linkmen).send_keys('小黑')
        self.xpath_element(R().enter_message_phone).send_keys(13855679542)
        self.xpath_element(R().enter_message_sub).click()
        self.driver.switch_to.default_content()
        sleep(5)

    # 删除
    def customer_opertion_delete(self):
        self.driver.switch_to.frame(R().customer_frame)
        self.xpath_element(R().customer_select).click()
        sleep(2)
        self.xpath_element(R().customer_delete).click()
        self.xpath_element(R().customer_delete_sure).click()
        self.driver.switch_to.default_content()
        sleep(5)

    # 搜索
    def customer_opertion_search(self):
        self.driver.switch_to.frame(R().customer_frame)
        self.xpath_element(R().customer_search).send_keys('武汉市汉阳分局')
        self.xpath_element(R().customer_search_sub).click()
        self.driver.switch_to.default_content()
        sleep(5)

    # 我的客户
    def my_customer(self):
        self.xpath_element(R().my_customer).click()
        sleep(2)

    def my_customer_flow(self):
        self.main()
        self.customer()
        self.my_customer()
        sleep(2)

    # 我的客户的数量
    def my_customer_num(self):
        self.driver.switch_to.frame(R().my_customer_frame)
        num = self.xpath_element(R().my_customer_num).text
        self.driver.switch_to.default_content()
        return num[1:3].strip()

    def my_customer_name(self):
        self.driver.switch_to.frame(R().my_customer_frame)
        name = self.xpath_element(R().my_customer_name).text
        self.driver.switch_to.default_content()
        return name

    # 增加
    def my_customer_add(self):
        self.driver.switch_to.frame(R().my_customer_frame)
        self.xpath_element(R().my_customer_add).click()
        self.driver.switch_to.default_content()
        sleep(2)

        # 输入框
        self.driver.switch_to.frame(R().enter_add_message_frame)
        self.xpath_element(R().enter_message_name).send_keys('江流儿')
        self.xpath_element(R().enter_message_unit).click()
        self.xpath_element(R().enter_message_ubit_select).click()
        sleep(2)
        self.xpath_element(R().enter_message_phone).send_keys(15877154432)
        self.xpath_element(R().enter_message_department).click()
        self.xpath_element(R().enter_message_department_select).click()
        sleep(2)
        self.xpath_element(R().enter_message_sub).click()
        self.driver.switch_to.default_content()
        sleep(2)

    # 编辑
    def my_customer_editor(self):
        self.driver.switch_to.frame(R().my_customer_frame)
        self.xpath_element(R().my_customer_editor_select).click()
        sleep(2)
        self.xpath_element(R().my_customer_editor).click()
        self.driver.switch_to.default_content()
        sleep(2)

        # 输入框
        self.driver.switch_to.frame(R().enter_editor_message_frame)
        self.xpath_element(R().enter_editor_message_name).clear()
        self.xpath_element(R().enter_editor_message_name).send_keys('tester123')
        self.xpath_element(R().enter_message_WeChat).send_keys(159876258)
        self.xpath_element(R().enter_message_Telephone).send_keys(848751029)
        self.xpath_element(R().enter_message_hobby).send_keys('看书')
        self.xpath_element(R().enter_message_address).send_keys('湖北省武汉市汉阳区')
        self.xpath_element(R().enter_message_sub).click()
        self.driver.switch_to.default_content()
        sleep(5)

    # 删除
    def my_customer_delete(self):
        self.driver.switch_to.frame(R().my_customer_frame)
        self.xpath_element(R().my_customer_delete_select).click()
        sleep(2)
        self.xpath_element(R().my_customer_delete).click()
        sleep(2)
        self.xpath_element(R().my_customer_delete_sub).click()
        self.driver.switch_to.default_content()
        sleep(5)

    def my_customer_search(self):
        self.driver.switch_to.frame(R().my_customer_frame)
        self.xpath_element(R().my_customer_search).send_keys('江流儿')
        sleep(2)
        self.xpath_element(R().my_customer_search_sub).click()
        sleep(2)
        self.driver.switch_to.default_content()
        sleep(2)

    # 退出浏览器
    def cms_close(self):
        self.driver.quit()


c = CMS()
c.login(Y().data()['username'], Y().data()['password'])
# c.main()
# c.customer()
# c.customer_unit()
# c.customer_opertion_add()
# c.customer_opertion_editor()
# sleep(5)
# c.customer_opertion_delete()
# c.customer_opertion_search()
# sleep(5)
# c.cms_close()
# c.my_customer_flow()
# c.my_customer_add()
# print(c.my_customer_num())
# c.my_customer_editor()
# print(c.my_customer_name())
