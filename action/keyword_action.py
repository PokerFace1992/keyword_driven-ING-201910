#encoding=utf-8
import time
from selenium import webdriver
from proj_var.var import *
from util.find import *
from util.calendar import *
from util.log import *

driver = ""
def open(browser):
    global driver
    try:
        if browser.find("ie")>=0:
            driver = webdriver.Ie(executable_path=ieDriverFilePath)
        elif browser.find("chrome")>=0:
            driver = webdriver.Chrome(executable_path=chromeDriverFilePath)
        else:
            driver = webdriver.Firefox(executable_path=firefoxDriverFilePath)
    except Exception as e:
        error("open error: %s" % e)
        raise e

def visit(url):
    global driver
    driver.get(url)

def sleep(times):
    try:
        time.sleep(int(times))
    except Exception as e:
        error("sleep error: %s" % e)
        raise e

def input(locator_method,locator_exp,content):
    try:
        element = getElement(driver,locator_method,locator_exp)
        element.send_keys(content)
    except Exception as e:
        error("input error: %s" % e)
        raise  e

def click(locator_method,locator_exp):
    global driver
    try:
        element = getElement(driver,locator_method,locator_exp)
        element.click()
    except Exception as e:
        error("click error: %s" % e)
        raise e


def click_sign_in(locator_method, locator_exp):
    global driver
    try:
        element = getElement(driver, locator_method, locator_exp)
        element.click()
        time.sleep(1)
        assert_word("签到成功")
        i_know_btn = getElement(driver, 'xpath', '//a[@class="mod_popup_btn "]')
        i_know_btn.click()
    except Exception as e:
        is_clickable = element.get_attribute("class")
        if is_clickable != "sign_button disable":
            error("click_signin error: %s" % e)
            raise e


def assert_word(content):
    global driver
    try:
        assert content in driver.page_source
    except AssertionError as e:
        error("assert_word error: %s" % e)
        raise e

def assert_keyword(locator_method,locator_exp,keyword):
    global driver
    try:
        element = getElement(driver,locator_method,locator_exp)
        print(element.get_attribute('textContent'))
        assert keyword in element.get_attribute('textContent')
    except Exception as e:
        error("assert_keyword error: %s" % e)
        raise e

def quit():
    try:
        driver.quit()
    except Exception as e:
        error("quit error: %s" % e)
        raise e

def capture(file_path):
    try:
        driver.save_screenshot(file_path)
    except Exception as e:
        error("capture error: %s" % e)
        raise e

if __name__ == "__main__":
    open("chrome")
    visit("https://www.midea.cn/10000/1000000000100511253663.html")
    # sleep(1)
    # input("id", "query", "自动化测试")
    # click("id","stb")
    # sleep(3)
    # assert_word("安全测试")
    # capture(ProjDirPath + "\\screen_capture\\" + get_current_time() + ".png")
    assert_keyword('xpath','//b[@class="price"]','299')
    quit()

