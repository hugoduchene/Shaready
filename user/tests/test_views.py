from django.test import TestCase, Client
from django.urls import reverse
from user.models import CustomUser

""" unit test on user's views """


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.feed_url = reverse('feed')
        self.login_url = reverse('login')
        self.account_url = reverse('account', args=[1])
        self.myaccount_url = reverse('myaccount', args=[1])
        self.parameter_url = reverse('parameter')
        self.search_url = reverse('search')
        self.legal_notice_url = reverse('legal_notice')

    def test_get_home(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/home.html')

    def test_post_home(self):
        form_data = {
            'username': 'TestUsername',
            'email': 'Test@gmail.com',
            'password1': 'Secret123456',
            'password2': 'Secret123456',
        }

        response = self.client.post(self.home_url, form_data)
        self.assertRedirects(response, self.feed_url, status_code=302)

    def test_bad_post_home(self):
        form_data = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
        }
        response = self.client.post(self.home_url, form_data)
        self.assertTemplateUsed(response, 'user/home.html')

    def test_get_login(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/login.html')

    def test_get_home_unauthenticated(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        response = self.client.get(self.home_url)

        self.assertRedirects(response, self.feed_url, status_code=302)

    def test_get_account_authenticated(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        id_user = CustomUser.objects.all()[0].id
        account_url = reverse('account', args=[id_user])
        response = self.client.get(account_url)

        self.assertTemplateUsed(response, 'user/account.html')

    def test_get_account_unauthenticated(self):
        response = self.client.get(self.account_url)

        self.assertRedirects(response, self.home_url, status_code=302)

    def test_get_myaccount_authenticated_with_good_id(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        id_user = CustomUser.objects.all()[0].id
        myaccount_url = reverse('myaccount', args=[id_user])
        response = self.client.get(myaccount_url)

        self.assertTemplateUsed(response, 'user/myaccount.html')

    def test_get_myaccount_with_bad_id(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        CustomUser(username="OtherUser").save()
        myaccount_url = reverse('myaccount', args=[CustomUser.objects.all()[1].id])
        account_url = reverse('account', args=[CustomUser.objects.all()[1].id])
        response = self.client.get(myaccount_url)

        self.assertRedirects(response, account_url, status_code=302)

    def test_get_myaccount_unauthenticated(self):
        response = self.client.get(self.myaccount_url)

        self.assertRedirects(response, self.home_url, status_code=302)

    def test_get_paramter_account_authenticated(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        response = self.client.get(self.parameter_url)

        self.assertTemplateUsed(response, 'user/ParameterAccount.html')

    def test_get_parameter_unauthenticated(self):
        response = self.client.get(self.parameter_url)

        self.assertRedirects(response, self.home_url, status_code=302)

    def test_get_search_unauthenticated(self):
        response = self.client.get(self.search_url)

        self.assertRedirects(response, self.home_url, status_code=302)

    def test_get_search_authenticated(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        response = self.client.get(self.search_url)

        self.assertTemplateUsed(response, 'user/search_user.html')

    def test_get_legal_notice(self):
        response = self.client.get(self.legal_notice_url)

        self.assertTemplateUsed(response, 'cgu/legalnotice.html')
