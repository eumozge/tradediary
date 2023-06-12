from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from helpers.db import LowerCharField

__all__ = ('TransactionType', 'Transaction', 'AccountType', 'Account')


class TransactionType(models.Model):
    name = LowerCharField(unique=True)

    class Meta:
        verbose_name = _('transaction type')
        verbose_name_plural = _('transaction types')

    def __str__(self):
        return self.name


class Transaction(models.Model):
    type = models.ForeignKey(
        'accounts.TransactionType',
        on_delete=models.PROTECT,
        verbose_name=_('type')
    )
    amount = models.DecimalField(_('price'), max_digits=20, decimal_places=12, default=0)
    creation_date = models.DateTimeField(_('creation date'), default=timezone.now, db_index=True)

    class Meta:
        verbose_name = _('transaction')
        verbose_name_plural = _('transactions')


class AccountType(models.Model):
    name = LowerCharField(unique=True)

    class Meta:
        verbose_name = _('account type')
        verbose_name_plural = _('account types')

    def __str__(self):
        return self.name


class Account(models.Model):
    type = models.ForeignKey(
        'accounts.AccountType',
        on_delete=models.PROTECT,
        verbose_name=_('type')
    )
    amount = models.DecimalField(_('amount'), max_digits=8, decimal_places=2, default=0)
    date = models.DateField(_('date'), default=timezone.now, db_index=True)

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
