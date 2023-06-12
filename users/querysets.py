from django.db import models


class AppUserQuerySet(models.QuerySet):
    def _get_or_create(self, email, **kwargs):
        email = email.lower()
        if self.filter(email=email):
            return self.get(email=email)
        return self.create(email=email, **kwargs)
