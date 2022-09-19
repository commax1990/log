from django.db import models


class load(models.Model):
    list_status = [
        ('open', 'open'),
        ('delivered', 'delivered'),
        ('INVOICED', 'INVOICED'),
        ('Paid', 'Paid'),
    ]

    itsnumber = models.IntegerField(verbose_name='ITS number')
    driver = models.ForeignKey('driver', on_delete=models.PROTECT,
                               null=True, verbose_name='Driver')
    Company = models.ForeignKey('Company', on_delete=models.PROTECT,
                                null=True, verbose_name='Company')
    load = models.IntegerField(verbose_name='#')
    truck = models.ForeignKey('truck', on_delete=models.PROTECT,
                              null=True, verbose_name='Truck')
    trailer = models.ForeignKey('trailer', on_delete=models.PROTECT,
                                null=True, verbose_name='Trailer')
    status = models.CharField(max_length=9, choices=list_status, default='open')
    # ship_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    # delivery_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    dispatcher = models.ForeignKey('dispatcher', on_delete=models.PROTECT,
                                   null=True, verbose_name='Dispatcher')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'List load'
        verbose_name_plural = 'List load'


class driver(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='First name')
    last_name = models.CharField(max_length=150, verbose_name='Last name')

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'Driver'


class company(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    mcnumber = models.CharField(max_length=10, verbose_name='MC number')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'


class truck(models.Model):
    unit_number = models.CharField(max_length=150, verbose_name='Unit Number')
    plate_number = models.CharField(max_length=10, verbose_name='Plate Number')

    def __str__(self):
        return self.unit_number

    class Meta:
        verbose_name = 'Truck'


class trailer(models.Model):
    unit_number = models.CharField(max_length=150, verbose_name='Unit Number')
    plate_number = models.CharField(max_length=10, verbose_name='Plate Number')

    def __str__(self):
        return self.unit_number

    class Meta:
        verbose_name = 'Trailer'


class dispatcher(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='First name')
    last_name = models.CharField(max_length=150, verbose_name='Last name')

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'Dispatcher'
