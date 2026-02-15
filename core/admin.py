from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date_envoi', 'lu')
    list_filter = ('lu', 'date_envoi')
    search_fields = ('nom', 'email', 'sujet', 'message')
    readonly_fields = ('date_envoi',)
    list_editable = ('lu',)
