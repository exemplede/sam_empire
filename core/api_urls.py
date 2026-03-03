from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r'articles', api_views.ArticleViewSet)
router.register(r'temoignages', api_views.TemoignageViewSet)
router.register(r'messages', api_views.ContactMessageViewSet)

urlpatterns = [
    path('login/', api_views.api_login, name='api_login'),
    path('logout/', api_views.api_logout, name='api_logout'),
    path('dashboard/', api_views.api_dashboard, name='api_dashboard'),
    path('', include(router.urls)),
]
