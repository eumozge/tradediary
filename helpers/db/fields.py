from django.db import models

__all__ = ('LowerCharField', 'UpperCharField')


class LowerCharField(models.CharField):
    def get_prep_value(self, value):
        return super().get_prep_value(value).lower()


class UpperCharField(models.CharField):
    def get_prep_value(self, value):
        return super().get_prep_value(value).upper()
