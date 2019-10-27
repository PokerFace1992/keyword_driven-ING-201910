#encoding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from util.log import *

# 获取单个页面元素对象
def getElement(driver, locationType, locatorExpression):
    try:
        element = WebDriverWait(driver, 10).until\
            (lambda x: x.find_element(by=locationType, value = locatorExpression))
        return element
    except Exception as err:
        error(err)
        raise err

# 获取多个相同页面元素对象，以list返回
def getElements(driver, locationType, locatorExpression):
    try:
        elements = WebDriverWait(driver, 10).until\
            (lambda x:x.find_elements(by=locationType, value = locatorExpression))
        return elements
    except Exception as err:
        error(err)
        raise err

if __name__ == '__main__':
    from selenium import webdriver
    # 进行单元测试
    driver = webdriver.Chrome(executable_path="g:\\chromedriver")
    driver.maximize_window()
    driver.get("http://www.midea.cn")
    # searchBox = getElement(driver, "id", "kw")
    login_button = getElement(driver, "id", "unloginStatus")
    # 打印页面对象的标签名
    # print(searchBox.tag_name)
    login_button.click()
    import time
    time.sleep(2)
    # print(login_button.tar_name)
    # aList = getElements(driver, "tag name", "a")
    # print(len(aList))
    driver.quit()