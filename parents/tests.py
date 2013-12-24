from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from parents.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
        #self.assertTrue(response.content.startswith(b'<html>'))
        #print(response.content)
        #self.assertIn(b'<title>ParentsSay</title>', response.content)
        #self.assertTrue(response.content.strip().endswith(b'</html>'))
    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['parents_content'] = 'I love you littletp.'
        request.POST['role'] = '父'
        request.POST['baby_name'] = 'littletp'

        response = home_page(request)

        self.assertIn('2013-12-18 父:I love you littletp.@littletp', 
                      response.content.decode())
        expected_html = render_to_string(
            'home.html', {
                'new_content_text':
                '2013-12-18 父:I love you littletp.@littletp'
            }
        )
        self.assertEqual(response.content.decode(), expected_html)

