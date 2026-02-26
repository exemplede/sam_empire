from django.db import models
from django.utils.text import slugify


class Article(models.Model):
    """Articles d'actualité publiés par l'administrateur."""
    titre = models.CharField(max_length=200, verbose_name="Titre de l'article")
    slug = models.SlugField(max_length=220, unique=True, blank=True, verbose_name="Slug URL")
    contenu = models.TextField(verbose_name="Contenu")
    resume = models.CharField(max_length=300, verbose_name="Résumé court",
                              help_text="Affiché sur la page d'accueil (max 300 caractères)")
    image = models.ImageField(upload_to='articles/', blank=True, null=True, verbose_name="Image de couverture")
    icone = models.CharField(max_length=10, default='📰', verbose_name="Icône emoji",
                             help_text="Utilisée si pas d'image (ex: 📰 🎥 🚀 🏆)")
    date_publication = models.DateTimeField(verbose_name="Date de publication")
    publie = models.BooleanField(default=True, verbose_name="Publié")
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_publication']
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titre) or 'article'
            slug = base_slug
            n = 1
            while Article.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

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


class Temoignage(models.Model):
    """Témoignages clients avec capture d'écran."""
    nom_client = models.CharField(max_length=150, verbose_name="Nom du client")
    entreprise = models.CharField(max_length=150, blank=True, verbose_name="Entreprise / Secteur")
    texte = models.TextField(verbose_name="Texte du témoignage",
                             help_text="Court résumé affiché sur la page contact")
    image = models.ImageField(upload_to='temoignages/', verbose_name="Capture d'écran du témoignage")
    publie = models.BooleanField(default=True, verbose_name="Publié")
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_creation']
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"

    def __str__(self):
        return f"{self.nom_client} — {self.entreprise or 'Client'}"
