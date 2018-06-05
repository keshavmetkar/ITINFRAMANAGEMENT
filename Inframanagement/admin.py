from django.contrib import admin
from .models import Ups, PowerSource,Location,Rack,Orgnization


class RackTabluarInline(admin.TabularInline):
    model = Rack
    max_num = 1

class UpsTabluarInline(admin.TabularInline):
    model = Ups
    max_num = 1

class LocationAdmin(admin.ModelAdmin):
    inlines= [UpsTabluarInline,RackTabluarInline]
    class Meta:
        model =Location

# Register your models here.
admin.site.register(Ups)
admin.site.register(PowerSource)
admin.site.register(Location,LocationAdmin)
admin.site.register(Rack)
admin.site.register(Orgnization)