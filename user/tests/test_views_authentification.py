from django.test import TestCase, Client
from django.urls import reverse
from user.models import CustomUser
from user.forms import RegistrationForm

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.feed_url = reverse('feed')
        self.login_url = reverse('login')

    def test_get_home(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/home.html')
    
    def test_post_home(self):
        form_data = {
            'username' : 'TestUsername',
            'email' : 'Test@gmail.com',
            'password1' : 'Secret123456',
            'password2' : 'Secret123456',
        }
        
        response = self.client.post(self.home_url, form_data)
        self.assertRedirects(response, self.feed_url, status_code=302)

    def test_bad_post_home(self):
        form_data = {
            'username' : '',
            'email' : '',
            'password1' : '',
            'password2' : '',
        }
        response = self.client.post(self.home_url, form_data)
        self.assertTemplateUsed(response, 'user/home.html')

    def test_get_login(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '../templates/user/connexion.html')
    

        



