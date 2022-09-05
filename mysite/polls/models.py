from django.db import models


class Spisok_MC_Number(models.Model):
    mcnumber = models.TextField(blank=50, verbose_name='name')

    def __str__(self):
        return self.mcnumber

    class Meta:
        verbose_name = 'mcnumber'
        verbose_name_plural = 'mcnumber'
        ordering = ['mcnumber']
