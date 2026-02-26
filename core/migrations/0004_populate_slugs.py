from django.db import migrations, models
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    Article = apps.get_model('core', 'Article')
    for article in Article.objects.filter(slug=''):
        base = slugify(article.titre) or 'article'
        slug = base
        n = 1
        while Article.objects.filter(slug=slug).exclude(pk=article.pk).exists():
            slug = f"{base}-{n}"
            n += 1
        article.slug = slug
        article.save(update_fields=['slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_article_slug'),
    ]

    operations = [
        migrations.RunPython(populate_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=220, unique=True),
        ),
    ]
