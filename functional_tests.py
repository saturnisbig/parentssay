from selenium import webdriver
#import unittest
# 2013-12-13 18:48:00 
# 在确定怀上孩子的第一天，夫妻双方约定每天对自己的宝宝说一句话。
# Teddy 现在是一名准爸爸，每天都会将相对宝宝说的话记在本子上。
# Teddy想是否有这样一个应用，供夫妻使用，准爸爸、准妈妈每天分别
# 将想对宝宝说的话贴到网上，彼此不能看见对方对宝宝说的话，等宝宝
# 出生后，可以让宝宝自己上去看。
# 父母需要注册、登录，需要为宝宝注册帐号(查看历史记录)
## 父母不用注册、登录，只需在写完的句子后面@小孩的帐号即可。

browser = webdriver.Firefox()
# Teddy访问网站，看见网站标题写着"ParentsSay"
browser.get('http://localhost:8000')

#assert 'ParentsSay' in browser.title
assert 'Django' in browser.title

# 网站提供了一个文本输入框，供输入

# Teddy输入了今天相对宝宝说的话，blabla...，并@littleteddy后点击提交，

# 网站提示成功提交，并显示提交的内容

# Teddy关闭了浏览器



# 网站提示需要先注册
# Teddy进行了简单的注册后，页面跳转到刚才输入内容的状态
# 
# 2013-12-13 19:05:29 
