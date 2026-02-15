from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage


def index(request):
    """Page d'accueil - site vitrine one-page."""
    if request.method == 'POST':
        nom = request.POST.get('nom', '').strip()
        email = request.POST.get('email', '').strip()
        sujet = request.POST.get('sujet', '').strip()
        message_text = request.POST.get('message', '').strip()

        if nom and email and message_text:
            ContactMessage.objects.create(
                nom=nom,
                email=email,
                sujet=sujet or 'Sans sujet',
                message=message_text,
            )
            messages.success(request, 'Votre message a été envoyé avec succès ! Nous vous répondrons dans les plus brefs délais.')
            return redirect('index')
        else:
            messages.error(request, 'Veuillez remplir tous les champs obligatoires.')

    return render(request, 'core/index.html')
