from django.contrib import admin

from .models import driver, load, company, truck, trailer, dispatcher


class LoadAdmin(admin.ModelAdmin):
    list_display = ('itsnumber', 'driver', 'Company', 'load', 'truck', 'trailer', 'status', 'dispatcher')
    search_fields = ('itsnumber', 'driver', 'Company', 'load', 'truck', 'trailer', 'status', 'dispatcher')
    list_filter = ('itsnumber', 'driver', 'Company', 'load', 'truck', 'trailer', 'status', 'dispatcher')


class DriverAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'mcnumber')
    search_fields = ('name', 'mcnumber')
    list_filter = ('name', 'mcnumber')


class TruckAdmin(admin.ModelAdmin):
    list_display = ('unit_number', 'plate_number')
    search_fields = ('unit_number', 'plate_number')
    list_filter = ('unit_number', 'plate_number')


class TrailerAdmin(admin.ModelAdmin):
    list_display = ('unit_number', 'plate_number')
    search_fields = ('unit_number', 'plate_number')
    list_filter = ('unit_number', 'plate_number')


class DispatcherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')


admin.site.register(load, LoadAdmin)
admin.site.register(driver, DriverAdmin)
admin.site.register(company, CompanyAdmin)
admin.site.register(truck, TruckAdmin)
admin.site.register(trailer, TrailerAdmin)
admin.site.register(dispatcher, DispatcherAdmin)
