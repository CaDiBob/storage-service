from django.db import models


class Part(models.Model):
    name = models.CharField(
        'Наименование',
        max_length=150,
        db_index=True,
    )
    code = models.CharField(
        'Код по ГК',
        max_length=15,
        db_index=True,
    )

    class Meta:
        verbose_name = 'ЗИП'
        verbose_name_plural = 'ЗИП'

    def __str__(self):
        return f'{self.code}'


class Order(models.Model):
    created_td = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        verbose_name = 'Требование'
        verbose_name_plural = 'Требования'

    def __str__(self):
        return f'self.created_td'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        models.CASCADE,
        related_name='items',
        verbose_name='Требование',
        db_index=True,
    )
    part = models.ForeignKey(
        Part,
        models.CASCADE,
        related_name='items',
        verbose_name='ЗИП',
        db_index=True,
    )

    class Meta:
        verbose_name = 'Пункты требования'
        verbose_name_plural = 'Пункты требований'

    def __str__(self):
        return f'{self.order.created_td}'
