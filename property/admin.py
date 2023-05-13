from django.contrib import admin

from .models import Complaint, Flat, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    raw_id_fields = ('liked_by',)
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town', 'owner_pure_phone']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']


@admin.register(Complaint)
class ComplaintsAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')
    list_display = ['user', 'flat', 'description']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ('name', 'phonenumber', 'pure_phone',)
