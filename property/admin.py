from django.contrib import admin

from .models import Complaint, Flat, Owner


class FlatInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ("owner", "flat",)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    raw_id_fields = ('liked_by',)
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']


@admin.register(Complaint)
class ComplaintsAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')
    list_display = ['user', 'flat', 'description']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    search_fields = ('name',)
    list_display = ('name', 'phonenumber', 'pure_phone',)
    inlines = [FlatInline, ]
