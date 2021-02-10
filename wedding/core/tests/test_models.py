from django.test import TestCase

from wedding.core import models


class UserTestCase(TestCase):
    required_user_attrs = {
        'username': 'User0001',
        'password': 'Password001'
    }

    def test_is_staff_flag_set_on_admin_user_type(self):
        data = {**self.required_user_attrs, 'user_type': models.User.UserTypes.ADMIN}
        user = models.User.objects.create_user(**data)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.admin)

    def test_is_staff_flag_set_on_newlywed_user_type(self):
        data = {**self.required_user_attrs, 'user_type': models.User.UserTypes.NEWLYWED}
        user = models.User.objects.create_user(**data)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.admin)
