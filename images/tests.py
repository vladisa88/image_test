from django.test import TestCase
from django.urls import reverse


class ListPageTests(TestCase):

    def test_list_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_name(self):
        response = self.client.get(reverse('list'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(template_name='images/image/list.html')

    def test_list_page_contains_correct_item(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Django Image Uploading</h1>')

    def test_list_page_not_contain_incorrect_item(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Shrek, please be there')


class UploadPageTests(TestCase):

    def test_upload_page_status_code(self):
        response = self.client.get('/upload/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_name(self):
        response = self.client.get(reverse('create'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(template_name='images/image/create.html')

    def test_upload_page_contains_correct_item(self):
        response = self.client.get('/upload/')
        self.assertContains(response, '<h1>Uploading image</h1>')

    def test_upload_page_not_contain_incorrect_item(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Shrek, please be there')
