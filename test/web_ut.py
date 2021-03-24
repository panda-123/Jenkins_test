import allure
import configparser
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


@allure.feature('Test Baidu WebUI')
class ISelenium(unittest.TestCase):
    # 读入配置文件
    def get_config(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.environ['HOME'], 'iselenium.ini'))
        # config.read(r'C:\Users\isuser\iselenium.ini')
        return config

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        config = self.get_config()

        # 控制是否采用无界面形式运行自动化测试
        try:
            browser = os.environ["browser"]
        except KeyError:
            browser = None
            print('没有配置环境变量 browser, 按照默认有界面方式运行自动化测试')

        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        if browser is not None and browser.lower() == 'no_gui':
            print('使用无界面方式运行')
            chrome_options.add_argument("--headless")
            # chrome_options.add_argument("--no-sandbox")
            self.driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'),
                                           options=chrome_options)
        elif browser is not None and browser.lower() == 'remote':
            docker_remote = config.get('driver', 'remote')
            print(f'使用远程方式运行, remote url:{docker_remote}')
            self.driver = webdriver.Remote(command_executor=docker_remote,
                                           desired_capabilities=DesiredCapabilities.CHROME)
        else:
            print('使用有界面Chrome浏览器运行')
            chrome_options.add_argument("--no-sandbox")
            self.driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'),
                                           options=chrome_options)

    @allure.story('Test key word 今日头条')
    def test_webui_1(self):
        """ 测试用例1，验证'今日头条'关键词在百度上的搜索结果
        """

        self._test_baidu('今日头条', 'test_webui_1')

    @allure.story('Test key word 王者荣耀')
    def test_webui_2(self):
        """ 测试用例2， 验证'王者荣耀'关键词在百度上的搜索结果
        """

        self._test_baidu('王者荣耀', 'test_webui_2')

    def _test_baidu(self, search_keyword, testcase_name):
        """ 测试百度搜索子函数

        :param search_keyword: 搜索关键词 (str)
        :param testcase_name: 测试用例名 (str)
        """

        self.driver.get("https://www.baidu.com")
        print('打开浏览器，访问 www.baidu.com')
        time.sleep(5)
        assert f'百度一下' in self.driver.title

        elem = self.driver.find_element_by_name("wd")
        elem.send_keys(f'{search_keyword}{Keys.RETURN}')
        print(f'搜索关键词~{search_keyword}')

        time.sleep(5)
        result = f'{search_keyword}' in self.driver.title
        self.assertTrue(result, msg=f'{testcase_name}校验点 pass')

        if result:
            print(f'搜索关键词{search_keyword}: Pass')
        else:
            print(f'搜索关键词{search_keyword}: Fail')
