from django.contrib import admin
from .models import ContactMessage, Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication', 'publie', 'date_creation')
    list_filter = ('publie', 'date_publication')
    search_fields = ('titre', 'contenu', 'resume')
    list_editable = ('publie',)
    ordering = ('-date_publication',)
    fieldsets = (
        ('Contenu', {
            'fields': ('titre', 'resume', 'contenu')
        }),
        ('Visuel', {
            'fields': ('image', 'icone'),
            'description': "Ajoutez une image ou choisissez un emoji comme icône."
        }),
        ('Publication', {
            'fields': ('date_publication', 'publie')
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date_envoi', 'lu')
    list_filter = ('lu', 'date_envoi')
    search_fields = ('nom', 'email', 'sujet', 'message')
    readonly_fields = ('date_envoi',)
    list_editable = ('lu',)
