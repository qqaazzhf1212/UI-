from selenium import webdriver
from time import sleep
from util.readConfig import ReadIni as rd
import os
import sys
driver = webdriver.Chrome()


# 初始化浏览器
def driver_init():
    driver.get(rd().url)
    driver.maximize_window()
    sleep(2)


def get_element_xpath(xpath):
    xp_element = driver.find_element_by_xpath(xpath)
    return xp_element


def get_element_id(id):
    id_element = driver.find_element_by_id(id)
    return id_element


def get_element_class_name(class_name):
    cl_element = driver.find_element_by_class_name(class_name)
    return cl_element


def get_element_selector(selector):
    sl_element = driver.find_element_by_css_selector(selector)


# 登录
def login():
    get_element_id('username').send_keys('test001')
    get_element_id('password').send_keys(123456)
    get_element_class_name('dlk').click()
    sleep(2)


def logout():
    driver.quit()


# 首页下拉框
def main():
    get_element_xpath('//*[@id="main"]/div[1]/li[1]/i').click()
    sleep(2)


# 客户管理
def customer():
    get_element_xpath('//*[@id="main"]/div[2]/div/div[1]/ul/li[1]').click()
    sleep(2)


# 客户单位管理
def customer_one():
    get_element_xpath('//*[@id="main"]/div[2]/div/div[1]/ul/li[1]/ul/li[1]').click()
    sleep(2)


def customer_opertion_add():
    driver.switch_to.frame('0b57e756-dac2-45a2-9618-9e6d1405fb15')
    # 新增
    get_element_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div/button[1]').click()
    sleep(2)
    driver.switch_to.default_content()
    # 输入信息
    driver.switch_to.frame('addCustomerUnit')
    get_element_xpath('//*[@id="app"]/form/div[1]/div[1]/div/div/div/input').send_keys('武汉市分局')
    sleep(2)
    get_element_xpath('//*[@id="app"]/form/div[1]/div[2]/div/div/div/div[1]/div/input').click()
    sleep(2)
    get_element_xpath('//*[@id="app"]/form/div[1]/div[2]/div/div/div/div[2]/ul[2]/li[2]').click()
    sleep(2)
    get_element_xpath('//*[@id="app"]/form/div[2]/div[1]/div/div/div/div[1]/div/input').clear()
    get_element_xpath('//*[@id="app"]/form/div[2]/div[1]/div/div/div/div[1]/div/input').send_keys('机构')
    sleep(2)
    get_element_xpath('//*[@id="app"]/form/div[2]/div[2]/div/div/div[1]/input').send_keys('武汉市江汉区')
    sleep(2)
    get_element_xpath('//*[@id="app"]/form/div[3]/div[1]/div/div/div/input').send_keys('小黑')
    sleep(2)
    get_element_xpath('//*[@id="app"]/form/div[3]/div[2]/div/div/div/input').send_keys(13855679542)
    sleep(2)
    get_element_xpath('//*[@id="app"]/form/div[5]/div/div/div/button/i').click()
    get_element_xpath('//*[@id="app"]/form/div[5]/div/div/div/button/i').click()
    # driver.switch_to.parent_frame()
    driver.switch_to.default_content()
    # driver.refresh()
    sleep(2)


def customer_opertion_delete():
    driver.switch_to.frame('0b57e756-dac2-45a2-9618-9e6d1405fb15')
    get_element_xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr[6]/td[1]/div/label/span/input').click()
    get_element_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div/button[3]').click()
    get_element_xpath('/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]').click()
    driver.switch_to.default_content()
    sleep(2)


def customer_opertion_editor():
    driver.switch_to.frame('0b57e756-dac2-45a2-9618-9e6d1405fb15')
    get_element_xpath(
        '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/div/label/span/input').click()
    get_element_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div/button[2]').click()
    driver.switch_to.default_content()
    sleep(2)


driver_init()
login()
# main()
# customer()
# customer_one()
# customer_opertion_add()
# customer_opertion_delete()
# customer_opertion_editor()
# logout()
