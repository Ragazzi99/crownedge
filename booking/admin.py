from django.contrib import admin
from . models import *

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'room','room_num', 'booking_code', 'checkin', 'checkout', 'no_days', 'amount', 'paid', 'avaliable',  'checkout_update', 'future', 'display']
    readonly_fields = ['user', 'room','room_num', 'booking_code', 'checkin', 'checkout', 'no_days', 'amount', 'paid', ]




class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'amount', 'paid', 'phone', 'pay_code', 'booking_code', 'payment_date', 'admin_update', 'admin_note']
    readonly_fields = ['user', 'first_name', 'last_name', 'amount', 'paid', 'phone', 'pay_code']





admin.site.register(Booking,BookingAdmin)
admin.site.register(Payment,PaymentAdmin)