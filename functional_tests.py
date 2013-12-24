#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class ParentsVisitor(unittest.TestCase):
    """ test the behavior and state when parents visit this website """
    def setUp(self):
        self.browser = webdriver.Firefox()
        # wait for the website to response
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_can_input_and_display_content(self):
        # Teddy访问网站，看见网站标题写着"ParentsSay"
        self.browser.get("http://localhost:8000")
        #assert 'ParentsSay' in browser.title
        self.assertIn('ParentsSay', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('ParentsSay', header_text)

        # 网站提供了一个文本输入框，供输入
        # a textarea element.
        input_box = self.browser.find_element_by_id('id_new_content')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            '输入你想对宝宝说的话'
        )
        # a dropdown select element.
        input_select = self.browser.find_element_by_id('id_role')
        options = input_select.find_elements_by_tag_name('option')
        print([o.text for o in options])
        self.assertEqual(
            options[0].text,
            '父'
        )
        self.assertEqual(
            options[1].text,
            '母'
        )
        input_child_name = self.browser.find_element_by_id('id_child_name')
        self.assertEqual(
            input_child_name.get_attribute('placeholder'),
            '输入宝宝的用户名'
        )
        # Teddy输入了今天相对宝宝说的话，blabla...，并@littleteddy后点击提交，
        input_box.send_keys('blabla...')
        input_select.send_keys('父')
        input_child_name.send_keys('littletp')
        input_child_name.send_keys(Keys.ENTER)
        
        
        # 网站提示成功提交，并显示提交的内容
        table = self.browser.find_element_by_id('id_content_list')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            '2013-12-18 父: blabla...@littletp',
            [row.text for row in rows]
        )
        
        # Teddy关闭了浏览器
        self.fail('Finish the test.')
        
        
        
        # 网站提示需要先注册
        # Teddy进行了简单的注册后，页面跳转到刚才输入内容的状态
        # 

if __name__ == '__main__':
    unittest.main(warnings='ignore')
