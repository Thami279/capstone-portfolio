from django.contrib import admin

from . import models


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "display_order", "is_published")
    list_filter = ("is_published",)
    ordering = ("display_order",)
    search_fields = ("title", "summary")


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "color")
    search_fields = ("name",)


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "client_name", "status", "start_date", "end_date", "is_featured", "is_published")
    list_filter = ("status", "is_featured", "is_published", "service")
    search_fields = ("title", "client_name", "summary", "description")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
    ordering = ("-start_date",)


@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("client_name", "client_role", "is_featured", "is_published")
    list_filter = ("is_featured", "is_published")
    search_fields = ("client_name", "client_role", "quote")


@admin.register(models.ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "resolved")
    list_filter = ("resolved", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("created_at", "updated_at")
