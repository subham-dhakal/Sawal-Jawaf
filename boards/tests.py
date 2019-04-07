from django.test import TestCase
from django.urls import reverse
from django.core.urlresolvers import reverse
from. import views
# Create your tests here.

class HomeTest(TestCase):

    def test_home_view_status_code(self):
        url= reverse('home')
        response= self.client.get(url)
        self.assertEquals(response.status_code,200)

    def test_home_url_resolves(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

        