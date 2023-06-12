from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFit
from helpers.db import LowerCharField, UpperCharField

__all__ = ('Status', 'Symbol', 'PositionType', 'Position', 'PositionTypeResult', 'PositionResult', 'PositionImage')


class Status(models.Model):
    slug = LowerCharField(unique=True)

    class Meta:
        verbose_name = _('status')
        verbose_name_plural = _('statuses')
        ordering = ('slug',)

    def __str__(self):
        return self.slug


class Symbol(models.Model):
    name = UpperCharField(unique=True)

    class Meta:
        verbose_name = _('symbol')
        verbose_name_plural = _('symbols')
        ordering = ('name',)

    def __str__(self):
        return self.name


class PositionType(models.Model):
    name = LowerCharField(unique=True)

    class Meta:
        verbose_name = _('position type')
        verbose_name_plural = _('position types')
        ordering = ('name',)

    class Const:
        SELL = 'sell'
        BUY = 'sell'

    def __str__(self):
        return self.name

    def is_sell(self):
        return self.name.lower() == self.Const.SELL.lower()

    def is_buy(self):
        return self.name.lower() == self.Const.BUY.lower()


class Position(models.Model):
    status = models.ForeignKey(
        'trades.Status',
        on_delete=models.PROTECT,
        verbose_name=_('status')
    )
    symbol = models.ForeignKey(
        'trades.Symbol',
        on_delete=models.PROTECT,
        verbose_name=_('symbol')
    )
    type = models.ForeignKey(
        'trades.PositionType',
        on_delete=models.PROTECT,
        verbose_name=_('type')
    )
    opening_price = models.DecimalField(_('price'), max_digits=20, decimal_places=12, default=0)
    balance = models.DecimalField(_('balance'), max_digits=8, decimal_places=2, default=0)
    opening_date = models.DateTimeField(_('creation date'), default=timezone.now, db_index=True)

    class Meta:
        verbose_name = _('trade')
        verbose_name_plural = _('trades')
        ordering = ('-opening_date',)

    def __str__(self):
        return f'{self.symbol}({self.status}, {self.opening_date})'


class PositionTypeResult(models.Model):
    name = LowerCharField(unique=True)

    class Meta:
        verbose_name = _('type result')
        verbose_name_plural = _('type results')

    def __str__(self):
        return self.name


class PositionResult(models.Model):
    position = models.OneToOneField(
        'trades.Position',
        on_delete=models.CASCADE,
        verbose_name=_('trade')
    )
    type = models.ForeignKey(
        'trades.PositionTypeResult',
        on_delete=models.PROTECT,
        verbose_name=_('type')
    )
    closing_date = models.DateTimeField(_('creation date'), default=timezone.now, db_index=True)
    closing_price = models.DecimalField(_('price'), max_digits=20, decimal_places=12, default=0)
    price_percent = models.DecimalField(_('price percent'), max_digits=4, decimal_places=2, default=0)
    balance_percent = models.DecimalField(_('balance percent'), max_digits=4, decimal_places=2, default=0)
    pnl = models.DecimalField(_('pnl'), max_digits=10, decimal_places=6, default=0)

    class Meta:
        verbose_name = _('result')
        verbose_name_plural = _('results')

    @cached_property
    def opening_price(self):
        return self.position.opening_price

    @cached_property
    def is_sell(self):
        return self.position.type.is_sell

    def save(self, *args, **kwargs):
        delta = self.opening_price - self.closing_price if self.is_sell else self.closing_price - self.opening_price
        self.price_percent = delta / self.position.opening_price * 100
        self.balance_percent = self.pnl / self.position.balance * 100
        super().save(*args, **kwargs)


class PositionImage(models.Model):
    position = models.ForeignKey(
        'trades.Position',
        on_delete=models.CASCADE,
        verbose_name=_('position')
    )
    image = ProcessedImageField(
        upload_to='trades/images/',
        processors=[ResizeToFit(1280, 1280, upscale=False)],
        format='JPEG',
        options={'quality': 90},
        verbose_name=_('image'),
    )

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
