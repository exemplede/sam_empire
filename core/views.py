from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import ContactMessage, Article, Temoignage


def index(request):
    return render(request, 'core/index.html')

def page_apropos(request):
    return render(request, 'core/page_apropos.html')

def page_services(request):
    return render(request, 'core/page_services.html')

def page_equipe(request):
    return render(request, 'core/page_equipe.html')

def page_portfolio(request):
    return render(request, 'core/page_portfolio.html')

def page_contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom', '').strip()
        email = request.POST.get('email', '').strip()
        sujet = request.POST.get('sujet', '').strip()
        message_text = request.POST.get('message', '').strip()
        if nom and email and message_text:
            ContactMessage.objects.create(
                nom=nom, email=email,
                sujet=sujet or 'Sans sujet',
                message=message_text,
            )
            messages.success(request, 'Votre message a été envoyé avec succès !')
            return redirect('page_contact')
        else:
            messages.error(request, 'Veuillez remplir tous les champs obligatoires.')
    temoignages = Temoignage.objects.filter(publie=True)[:3]
    return render(request, 'core/page_contact.html', {'temoignages': temoignages})

def page_temoignages(request):
    temoignages = Temoignage.objects.filter(publie=True)
    return render(request, 'core/page_temoignages.html', {'temoignages': temoignages})

def articles_list(request):
    articles_qs = Article.objects.filter(publie=True)
    paginator = Paginator(articles_qs, 9)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'core/articles_list.html', {'articles': articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, publie=True)
    recents = Article.objects.filter(publie=True).exclude(pk=article.pk)[:4]
    return render(request, 'core/article_detail.html', {
        'article': article, 'recents': recents,
    })
