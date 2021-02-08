import factory

from wedding.core import models


class UserFactory(factory.Factory):
    class Meta:
        model = models.User
