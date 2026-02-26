from django.urls import path
from . import views

urlpatterns = [
    # Pages publiques (chaque section = sa propre page)
    path('', views.index, name='index'),
    path('a-propos/', views.page_apropos, name='page_apropos'),
    path('services/', views.page_services, name='page_services'),
    path('equipe/', views.page_equipe, name='page_equipe'),
    path('portfolio/', views.page_portfolio, name='page_portfolio'),
    path('contact/', views.page_contact, name='page_contact'),
    path('temoignages/', views.page_temoignages, name='page_temoignages'),
    # Articles publics
    path('actualites/', views.articles_list, name='articles_list'),
    path('actualites/<slug:slug>/', views.article_detail, name='article_detail'),
    # Espace gestion articles (client)
    path('gestion/', views.gestion_login, name='gestion_login'),
    path('gestion/logout/', views.gestion_logout, name='gestion_logout'),
    path('gestion/articles/', views.gestion_articles, name='gestion_articles'),
    path('gestion/articles/nouveau/', views.gestion_article_create, name='gestion_article_create'),
    path('gestion/articles/<int:pk>/modifier/', views.gestion_article_edit, name='gestion_article_edit'),
    path('gestion/articles/<int:pk>/supprimer/', views.gestion_article_delete, name='gestion_article_delete'),
    # Gestion témoignages
    path('gestion/temoignages/', views.gestion_temoignages, name='gestion_temoignages'),
    path('gestion/temoignages/nouveau/', views.gestion_temoignage_create, name='gestion_temoignage_create'),
    path('gestion/temoignages/<int:pk>/modifier/', views.gestion_temoignage_edit, name='gestion_temoignage_edit'),
    path('gestion/temoignages/<int:pk>/supprimer/', views.gestion_temoignage_delete, name='gestion_temoignage_delete'),
]
