#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ParentsVisitor(LiveServerTestCase):
    """ test the behavior and state when parents visit this website """
    def setUp(self):
        self.browser = webdriver.Firefox()
        # wait for the website to response
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_home_page_can_input_and_display_content(self):
        # Teddy访问网站，看见网站标题写着"ParentsSay"
        self.browser.get(self.live_server_url)
        #assert 'ParentsSay' in browser.title
        self.assertIn('ParentsSay', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Say Something To Your Baby', header_text)

        # 网站提供了一个文本输入框，供输入
        input_box = self.browser.find_element_by_id('id_new_entry')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            '输入你想对宝宝说的话'
        )
        # Teddy输入了今天相对宝宝说的话，blabla...，后点击提交，
        input_box.send_keys('blabla...')
        self.browser.find_element_by_id("id_submit").submit()
        
        # 网站提示成功提交，并显示提交的内容
        table = self.browser.find_element_by_id('id_entry_list')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            'blabla...',
            [row.text for row in rows]
        )

        # Teddy已经连续三天对宝宝说话了，他想看看自己前面几天写的内容
        input_box = self.browser.find_element_by_id('id_new_entry')
        input_box.send_keys('entry 1')
        self.browser.find_element_by_id('id_submit').submit()

        input_box = self.browser.find_element_by_id('id_new_entry')
        input_box.send_keys('entry 2')
        self.browser.find_element_by_id('id_submit').submit()
        table = self.browser.find_element_by_id('id_entry_list')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('entry 1', [row.text for row in rows])
        self.assertIn('entry 2', [row.text for row in rows])

        # Teddy关闭了浏览器
        self.fail('Finish the test.')
        # 网站提示需要先注册
        # Teddy进行了简单的注册后，页面跳转到刚才输入内容的状态
