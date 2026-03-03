from django.urls import path
from . import views

urlpatterns = [
    # Pages publiques
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
]
