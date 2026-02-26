from django.contrib import admin
from .models import ContactMessage, Article, Temoignage


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'slug', 'date_publication', 'publie', 'date_creation')
    list_filter = ('publie', 'date_publication')
    search_fields = ('titre', 'contenu', 'resume')
    list_editable = ('publie',)
    prepopulated_fields = {'slug': ('titre',)}
    ordering = ('-date_publication',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date_envoi', 'lu')
    list_filter = ('lu', 'date_envoi')
    search_fields = ('nom', 'email', 'sujet', 'message')
    readonly_fields = ('date_envoi',)
    list_editable = ('lu',)


@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('nom_client', 'entreprise', 'publie', 'date_creation')
    list_filter = ('publie',)
    list_editable = ('publie',)
