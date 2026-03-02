from django.contrib import admin
from .models import Resume, Portfolio, PortfolioImage, ContactModel


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 3  # shows 3 empty image slots by default in the admin


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at', 'resume')
    readonly_fields = ('uploaded_at',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'tools', 'github_link', 'live_link')
    search_fields = ('name', 'tools')
    inlines = [PortfolioImageInline]  # lets you add multiple images right inside the portfolio form


@admin.register(ContactModel)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email', 'message')