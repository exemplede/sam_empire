from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator
from .models import ContactMessage, Article, Temoignage


# =========================================
# PAGES PUBLIQUES (une par section)
# =========================================

def index(request):
    """Page d'accueil — Hero uniquement."""
    return render(request, 'core/index.html')


def page_apropos(request):
    """Page À Propos + Mission/Vision."""
    return render(request, 'core/page_apropos.html')


def page_services(request):
    """Page Services."""
    return render(request, 'core/page_services.html')


def page_equipe(request):
    """Page Équipe."""
    return render(request, 'core/page_equipe.html')


def page_portfolio(request):
    """Page Portfolio + Partenaires."""
    return render(request, 'core/page_portfolio.html')


def page_contact(request):
    """Page Contact + Témoignages + formulaire."""
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
    """Page galerie de tous les témoignages (captures d'écran)."""
    temoignages = Temoignage.objects.filter(publie=True)
    return render(request, 'core/page_temoignages.html', {'temoignages': temoignages})


# =========================================
# ARTICLES PUBLICS : LISTE + LECTURE
# =========================================

def articles_list(request):
    """Liste publique de tous les articles publiés."""
    articles_qs = Article.objects.filter(publie=True)
    paginator = Paginator(articles_qs, 9)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'core/articles_list.html', {'articles': articles})


def article_detail(request, slug):
    """Page de lecture d'un article."""
    article = get_object_or_404(Article, slug=slug, publie=True)
    recents = Article.objects.filter(publie=True).exclude(pk=article.pk)[:4]
    return render(request, 'core/article_detail.html', {
        'article': article, 'recents': recents,
    })


# =========================================
# ESPACE GESTION ARTICLES (CLIENT)
# =========================================

def gestion_login(request):
    """Page de connexion pour l'espace gestion."""
    if request.user.is_authenticated:
        return redirect('gestion_articles')
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('gestion_articles')
        else:
            messages.error(request, 'Identifiant ou mot de passe incorrect.')
    return render(request, 'core/gestion_login.html')


def gestion_logout(request):
    logout(request)
    return redirect('gestion_login')


@login_required(login_url='gestion_login')
def gestion_articles(request):
    """Dashboard articles."""
    articles = Article.objects.all()
    return render(request, 'core/gestion_articles.html', {'articles': articles})


@login_required(login_url='gestion_login')
def gestion_article_create(request):
    """Créer un article."""
    if request.method == 'POST':
        titre = request.POST.get('titre', '').strip()
        resume = request.POST.get('resume', '').strip()
        contenu = request.POST.get('contenu', '').strip()
        icone = request.POST.get('icone', '📰').strip()
        publie = request.POST.get('publie') == 'on'
        image = request.FILES.get('image')
        if titre and resume and contenu:
            article = Article(
                titre=titre, resume=resume, contenu=contenu,
                icone=icone or '📰', publie=publie,
                date_publication=timezone.now(), image=image,
            )
            article.save()
            messages.success(request, f'Article "{titre}" créé avec succès !')
            return redirect('gestion_articles')
        else:
            messages.error(request, 'Veuillez remplir le titre, le résumé et le contenu.')
    return render(request, 'core/gestion_article_form.html', {'mode': 'create'})


@login_required(login_url='gestion_login')
def gestion_article_edit(request, pk):
    """Modifier un article."""
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.titre = request.POST.get('titre', '').strip()
        article.resume = request.POST.get('resume', '').strip()
        article.contenu = request.POST.get('contenu', '').strip()
        article.icone = request.POST.get('icone', '📰').strip() or '📰'
        article.publie = request.POST.get('publie') == 'on'
        if request.FILES.get('image'):
            article.image = request.FILES['image']
        if article.titre and article.resume and article.contenu:
            article.save()
            messages.success(request, f'Article "{article.titre}" modifié !')
            return redirect('gestion_articles')
        else:
            messages.error(request, 'Veuillez remplir tous les champs obligatoires.')
    return render(request, 'core/gestion_article_form.html', {'mode': 'edit', 'article': article})


@login_required(login_url='gestion_login')
def gestion_article_delete(request, pk):
    """Supprimer un article."""
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        titre = article.titre
        article.delete()
        messages.success(request, f'Article "{titre}" supprimé.')
        return redirect('gestion_articles')
    return render(request, 'core/gestion_article_confirm.html', {'article': article})


# =========================================
# GESTION TÉMOIGNAGES
# =========================================

@login_required(login_url='gestion_login')
def gestion_temoignages(request):
    """Liste des témoignages."""
    temoignages = Temoignage.objects.all()
    return render(request, 'core/gestion_temoignages.html', {'temoignages': temoignages})


@login_required(login_url='gestion_login')
def gestion_temoignage_create(request):
    """Ajouter un témoignage."""
    if request.method == 'POST':
        nom_client = request.POST.get('nom_client', '').strip()
        entreprise = request.POST.get('entreprise', '').strip()
        texte = request.POST.get('texte', '').strip()
        publie = request.POST.get('publie') == 'on'
        image = request.FILES.get('image')
        if nom_client and texte and image:
            Temoignage.objects.create(
                nom_client=nom_client, entreprise=entreprise,
                texte=texte, publie=publie, image=image,
            )
            messages.success(request, f'Témoignage de "{nom_client}" ajouté !')
            return redirect('gestion_temoignages')
        else:
            messages.error(request, 'Veuillez remplir le nom, le texte et ajouter une image.')
    return render(request, 'core/gestion_temoignage_form.html', {'mode': 'create'})


@login_required(login_url='gestion_login')
def gestion_temoignage_edit(request, pk):
    """Modifier un témoignage."""
    temoignage = get_object_or_404(Temoignage, pk=pk)
    if request.method == 'POST':
        temoignage.nom_client = request.POST.get('nom_client', '').strip()
        temoignage.entreprise = request.POST.get('entreprise', '').strip()
        temoignage.texte = request.POST.get('texte', '').strip()
        temoignage.publie = request.POST.get('publie') == 'on'
        if request.FILES.get('image'):
            temoignage.image = request.FILES['image']
        if temoignage.nom_client and temoignage.texte:
            temoignage.save()
            messages.success(request, f'Témoignage modifié !')
            return redirect('gestion_temoignages')
        else:
            messages.error(request, 'Veuillez remplir les champs obligatoires.')
    return render(request, 'core/gestion_temoignage_form.html', {'mode': 'edit', 'temoignage': temoignage})


@login_required(login_url='gestion_login')
def gestion_temoignage_delete(request, pk):
    """Supprimer un témoignage."""
    temoignage = get_object_or_404(Temoignage, pk=pk)
    if request.method == 'POST':
        temoignage.delete()
        messages.success(request, 'Témoignage supprimé.')
        return redirect('gestion_temoignages')
    return render(request, 'core/gestion_temoignage_confirm.html', {'temoignage': temoignage})
