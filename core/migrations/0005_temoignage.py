from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_populate_slugs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temoignage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_client', models.CharField(max_length=150, verbose_name='Nom du client')),
                ('entreprise', models.CharField(blank=True, max_length=150, verbose_name='Entreprise / Secteur')),
                ('texte', models.TextField(help_text='Court résumé affiché sur la page contact', verbose_name='Texte du témoignage')),
                ('image', models.ImageField(upload_to='temoignages/', verbose_name="Capture d'écran du témoignage")),
                ('publie', models.BooleanField(default=True, verbose_name='Publié')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Témoignage',
                'verbose_name_plural': 'Témoignages',
                'ordering': ['-date_creation'],
            },
        ),
    ]
