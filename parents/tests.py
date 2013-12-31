from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from parents.views import home_page
from parents.models import Entry

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

        response = home_page(request)

        words = 'I love you littletp.'
        self.assertEqual(Entry.objects.all().count(), 1)
        new_entry = Entry.objects.all()[0]
        self.assertEqual(new_entry.what, words)

    def test_home_page_redirect_after_POST(self):
        """"""
        request = HttpRequest()
        request.method = 'POST'
        request.POST['parents_content'] = 'I love you littletp.'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_home_page_only_saves_entries_when_necessary(self):
        """"""
        request = HttpRequest()
        home_page(request)

        self.assertEqual(Entry.objects.all().count(), 0)

    def test_home_page_displays_all_list_entries(self):
        """"""
        Entry.objects.create(what='entry 1')
        Entry.objects.create(what='entry 2')

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('entry 1', response.content.decode())
        self.assertIn('entry 2', response.content.decode())


class EntryModelTest(TestCase):
    
    def test_can_saving_and_retrieving_entries(self):
        """"""
        first_entry = Entry.objects.create(what="First entry")

        second_entry = Entry.objects.create(what="Second entry")

        saved_entries = Entry.objects.all()
        self.assertEqual(saved_entries.count(), 2)

        first_saved_entry = saved_entries[0]
        second_saved_entry = saved_entries[1]

        self.assertEqual(first_saved_entry.what, 'First entry')
        self.assertEqual(second_saved_entry.what, 'Second entry')
        
