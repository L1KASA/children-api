import re

from django.db import models


class Child(models.Model):
    class Status(models.TextChoices):
        LEAD = 'lead', 'Лид'
        CLIENT = 'client', 'Клиент'

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=100,
        help_text='Имя ребенка'
    )

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=100,
        help_text='Фамилия ребенка'
    )

    middle_name = models.CharField(
        verbose_name='Отчество',
        max_length=100,
        blank=True,
        null=True,
        help_text='Отчество ребенка'
    )

    cyberons = models.PositiveIntegerField(
        verbose_name='Количество киберонов',
        default=0,
        help_text='Количество накопленных киберонов'
    )

    status = models.CharField(
        verbose_name='Статус',
        max_length=10,
        choices=Status.choices,
        default=Status.LEAD,
        help_text='Текущий статус ребенка'
    )

    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'
        ordering = ['last_name', 'first_name', '-created_at']

    def __str__(self) -> str:
        return f"{self.full_name} ({self.get_status_display()})"

    @property
    def full_name(self) -> str:
        """Свойство для ФИО ребенка"""
        if self.middle_name:
            return f"{self.last_name} {self.first_name} {self.middle_name}"
        return f"{self.last_name} {self.first_name}"
