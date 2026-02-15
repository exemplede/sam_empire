# 🏛️ SAM EMPIRE — Site Web Vitrine

Site web vitrine pour **SAM EMPIRE SARL**, agence de communication basée à Ouagadougou, Burkina Faso.

## 🚀 Installation & Lancement

### Prérequis
- Python 3.10+
- pip

### Étapes

```bash
# 1. Accéder au dossier du projet
cd sam_empire

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou: venv\Scripts\activate  # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Appliquer les migrations
python manage.py migrate

# 5. Créer un superutilisateur (pour l'admin)
python manage.py createsuperuser

# 6. Lancer le serveur
python manage.py runserver
```

### Accès
- **Site** : http://127.0.0.1:8000/
- **Admin** : http://127.0.0.1:8000/admin/

## 📁 Structure du projet

```
sam_empire/
├── manage.py
├── requirements.txt
├── sam_empire/          # Configuration Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/                # Application principale
│   ├── models.py        # Modèle ContactMessage
│   ├── views.py         # Vue index (accueil + formulaire)
│   ├── urls.py
│   ├── admin.py         # Admin pour les messages
│   └── apps.py
├── templates/
│   └── core/
│       └── index.html   # Template principal (one-page)
├── static/
│   ├── css/
│   │   └── style.css    # Styles CSS complets
│   ├── js/
│   │   └── main.js      # JavaScript (animations, navbar, etc.)
│   └── images/          # Dossier pour vos images
└── media/               # Fichiers uploadés
```

## 🎨 Personnalisation

### Ajouter vos images
Placez vos images dans `static/images/` et référencez-les dans le template avec :
```html
{% load static %}
<img src="{% static 'images/votre-image.jpg' %}" alt="Description">
```

### Modifier les couleurs
Éditez les variables CSS au début de `static/css/style.css` :
```css
:root {
    --primary-gold: #C8A84E;     /* Couleur principale */
    --dark-bg: #0A0A0F;          /* Fond principal */
    /* ... */
}
```

### Ajouter les logos partenaires
Remplacez les noms textuels dans la section "Partenaires" du template par des images de logos.

## 📧 Formulaire de Contact
Les messages envoyés via le formulaire sont stockés en base de données et visibles dans l'interface d'administration Django (`/admin/`).

## 🔒 Production
Avant le déploiement en production :
1. Changez `SECRET_KEY` dans `settings.py`
2. Mettez `DEBUG = False`
3. Configurez `ALLOWED_HOSTS`
4. Lancez `python manage.py collectstatic`

---

**SAM EMPIRE SARL** — *Donner à vos ambitions la dimension d'un empire*
