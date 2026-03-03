from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Article, Temoignage, ContactMessage
from .serializers import ArticleSerializer, TemoignageSerializer, ContactMessageSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    """Connexion — retourne un token d'authentification."""
    username = request.data.get('username', '')
    password = request.data.get('password', '')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'email': user.email or '',
        })
    return Response({'error': 'Identifiant ou mot de passe incorrect.'}, status=400)


@api_view(['POST'])
def api_logout(request):
    """Déconnexion — supprime le token."""
    if request.user and request.auth:
        request.auth.delete()
    return Response({'message': 'Déconnexion réussie.'})


@api_view(['GET'])
def api_dashboard(request):
    """Stats du dashboard."""
    return Response({
        'articles_total': Article.objects.count(),
        'articles_publies': Article.objects.filter(publie=True).count(),
        'temoignages_total': Temoignage.objects.count(),
        'messages_total': ContactMessage.objects.count(),
        'messages_non_lus': ContactMessage.objects.filter(lu=False).count(),
    })


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-date_publication')
    serializer_class = ArticleSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class TemoignageViewSet(viewsets.ModelViewSet):
    queryset = Temoignage.objects.all().order_by('-date_creation')
    serializer_class = TemoignageSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-date_envoi')
    serializer_class = ContactMessageSerializer
    http_method_names = ['get', 'patch', 'delete']

    @action(detail=True, methods=['patch'])
    def toggle_lu(self, request, pk=None):
        """Marquer/démarquer comme lu."""
        msg = self.get_object()
        msg.lu = not msg.lu
        msg.save()
        return Response(ContactMessageSerializer(msg).data)
