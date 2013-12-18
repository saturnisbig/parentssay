#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from selenium import webdriver
import unittest

# ----------- time spend ---------------
# 2013-12-13 18:48:00 2013-12-13 19:05:29
# 2013-12-14 15:26:46 2013-12-14 15:31:08
# 2013-12-14 23:13:39 2013-12-14 23:42:43
# 2013-12-18 12:35:11 2013-12-18 13:07:15
# 2013-12-18 21:31:05 
# --------------------------------------

# 在确定怀上孩子的第一天，夫妻双方约定每天对自己的宝宝说一句话。
# Teddy 现在是一名准爸爸，每天都会将相对宝宝说的话记在本子上。
# Teddy想是否有这样一个应用，供夫妻使用，准爸爸、准妈妈每天分别
# 将想对宝宝说的话贴到网上，彼此不能看见对方对宝宝说的话，等宝宝
# 出生后，可以让宝宝自己上去看。
# 父母需要注册、登录，需要为宝宝注册帐号(查看历史记录)
## 父母不用注册、登录，只需在写完的句子后面@小孩的帐号即可。

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
        print([o.text for o in input_select.options])
        self.assertEqual(
            options[0].text,
            '父'
        )
        self.assertEqual(
            options[1].text,
            '母'
        )
        input_child_name = self.find_element_by_id('id_child_name')
        self.assertEqual(
            input_child_name.text,
            'littletp'
        )
        # Teddy输入了今天相对宝宝说的话，blabla...，并@littleteddy后点击提交，
        input_box.send_keys('blabla...')
        input_select.send_keys('父')
        
        # 网站提示成功提交，并显示提交的内容
        table = self.browser.find_element_by_id('id_content_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            'blabla...',
            [row.text for row in rows]
        )
        
        # Teddy关闭了浏览器
        self.fail('Finish the test.')
        
        
        
        # 网站提示需要先注册
        # Teddy进行了简单的注册后，页面跳转到刚才输入内容的状态
        # 

if __name__ == '__main__':
    unittest.main(warnings='ignore')
