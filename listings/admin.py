from django.contrib import admin

from listings.models import Band, Listing


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'year')


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
