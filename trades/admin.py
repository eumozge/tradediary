from django.contrib import admin

from trades.models import *


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Symbol)
class SymbolAdmin(admin.ModelAdmin):
    pass


@admin.register(PositionType)
class PositionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(PositionTypeResult)
class PositionTypeResultAdmin(admin.ModelAdmin):
    pass


class PositionResultInlineAdmin(admin.StackedInline):
    model = PositionResult


class PositionImageInlineAdmin(admin.StackedInline):
    model = PositionImage


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'status', 'opening_date')
    list_display_links = ('symbol',)
    list_select_related = ('symbol', 'status')
    raw_id_fields = ('symbol',)
    inlines = (PositionResultInlineAdmin, PositionImageInlineAdmin)
