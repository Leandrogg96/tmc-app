from django.contrib import admin
from .models import Event, Activity, Photo, Sponsor, RecommendedRace
from django.utils.html import format_html

class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 1

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location')
    search_fields = ('name', 'location')
    list_filter = ('date',)
    inlines = [ActivityInline, PhotoInline]

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'event')
    search_fields = ('title',)
    list_filter = ('event',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('event', 'caption', 'preview')
    list_filter = ('event',)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    preview.short_description = "Preview"

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_preview')

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="100" />', obj.logo.url)
        return "-"
    logo_preview.short_description = "Logo"

@admin.register(RecommendedRace)
class RecommendedRaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    image_preview.short_description = "Image"
