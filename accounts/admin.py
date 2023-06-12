from django.contrib import admin

from accounts.models import * # noqa


@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'type', 'amount')
    list_select_related = ('type',)


@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date', 'amount', 'type')
    list_select_related = ('type',)
