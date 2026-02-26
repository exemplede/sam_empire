from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=220, unique=False),
            preserve_default=False,
        ),
    ]
