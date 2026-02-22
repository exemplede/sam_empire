from django.db import models


class Article(models.Model):
    """Articles d'actualité publiés par l'administrateur."""
    titre = models.CharField(max_length=200, verbose_name="Titre de l'article")
    contenu = models.TextField(verbose_name="Contenu")
    resume = models.CharField(max_length=300, verbose_name="Résumé court", help_text="Affiché sur la page d'accueil (max 300 caractères)")
    image = models.ImageField(upload_to='articles/', blank=True, null=True, verbose_name="Image de couverture")
    icone = models.CharField(max_length=10, default='📰', verbose_name="Icône emoji", help_text="Utilisée si pas d'image (ex: 📰 🎥 🚀 🏆)")
    date_publication = models.DateTimeField(verbose_name="Date de publication")
    publie = models.BooleanField(default=True, verbose_name="Publié")
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_publication']
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return f"{self.titre} ({self.date_publication.strftime('%d/%m/%Y')})"


class ContactMessage(models.Model):
    """Messages envoyés via le formulaire de contact."""
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_envoi']
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"

    def __str__(self):
        return f"{self.nom} - {self.sujet} ({self.date_envoi.strftime('%d/%m/%Y')})"
