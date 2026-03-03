from rest_framework import serializers
from .models import Article, Temoignage, ContactMessage


class ArticleSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'titre', 'slug', 'contenu', 'resume', 'image', 'image_url',
                  'icone', 'date_publication', 'publie', 'date_creation']
        read_only_fields = ['slug', 'date_creation']

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class TemoignageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Temoignage
        fields = ['id', 'nom_client', 'entreprise', 'texte', 'image', 'image_url',
                  'publie', 'date_creation']
        read_only_fields = ['date_creation']

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'nom', 'email', 'sujet', 'message', 'date_envoi', 'lu']
        read_only_fields = ['date_envoi']
