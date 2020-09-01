from django.test import TestCase
from user.forms import RegistrationForm

""" Unit test on forms """


class TestForms(TestCase):

    def test_registration_data(self):
        form = RegistrationForm(data={
            'username': 'TestUsername',
            'email': 'Test@gmail.com',
            'password1': 'Secret123456',
            'password2': 'Secret123456',
        })

        self.assertTrue(form.is_valid())

    def test_registration_no_data(self):
        form = RegistrationForm(data={
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
