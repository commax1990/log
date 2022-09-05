from django.db import models


class Spisok_MC_Number(models.Model):
    mcnumber = models.TextField(blank=50, verbose_name='MC Number')

    def __str__(self):
        return self.mcnumber

    class Meta:
        verbose_name = 'List MC Number'
        verbose_name_plural = 'List MC Number'
