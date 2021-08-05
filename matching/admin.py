from django.contrib import admin
from .models import Industry, Investor, StartDate, StartUP, Mail


class InvestorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)


class MailAdmin(admin.ModelAdmin):
    list_display = ('start_up', 'destination', 'sent', 'sent_date',)


class StartUPAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'industry', 'info', 'stage',)


admin.site.register(Industry)
admin.site.register(StartDate)
admin.site.register(StartUP, StartUPAdmin)
admin.site.register(Mail, MailAdmin)
admin.site.register(Investor, InvestorAdmin)
