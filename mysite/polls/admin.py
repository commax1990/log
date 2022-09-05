from django.contrib import admin

from .models import Spisok_MC_Number


class SpisokMCNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'mcnumber')
    search_fields = ('id', 'mcnumber')
    list_filter = ('mcnumber',)


admin.site.register(Spisok_MC_Number, SpisokMCNumberAdmin)
