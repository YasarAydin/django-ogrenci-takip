from django.contrib import admin
from . import models


# Register your models here.

"""class NotlarAdmin(admin.ModelAdmin):
    readonly_fields = ["ortalama", "durum"]"""


admin.site.register(models.Ogrenciler)
admin.site.register(models.Dersler)
admin.site.register(models.Kulupler)
admin.site.register(models.Notlar)
