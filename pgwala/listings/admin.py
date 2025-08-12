from django.contrib import admin
from .models import PGListing

@admin.register(PGListing)
class PGListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'rent', 'available_from', 'owner')
    search_fields = ('title', 'location')
