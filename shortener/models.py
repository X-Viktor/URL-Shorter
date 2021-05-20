from django.db import models


class ShortURL(models.Model):
    url = models.URLField(verbose_name='Ссылка')
    short_url = models.URLField(verbose_name='Короткая ссылка')

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return self.short_url
