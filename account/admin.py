from django.contrib import admin

from .models import CustomerProfile, EndUserProfile, EndUserInfo
# Register your models here.
admin.site.site_header = 'NFC Warehouse Administrator'

@admin.register(CustomerProfile)
class CustomerProfile(admin.ModelAdmin):
    list_display = ("birth", "phone", "address")
    list_filter = ("birth",)


@admin.register(EndUserProfile)
class EndUserProfile(admin.ModelAdmin):
    list_display = ("birth", "phone", "address")
    list_filter = ("birth",)


@admin.register(EndUserInfo)
class EndUserInfoAdmin(admin.ModelAdmin):
    list_display = ("user", "school", "company", "profession", "aboutme", "photo")
    list_filter = ("school", "company", "profession")

