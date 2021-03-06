# Generated by Django 2.1.7 on 2020-10-20 08:16

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201016_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimage',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='woman-playing.png', force_format=None, keep_meta=True, quality=100, size=[500, 500], upload_to=''),
        ),
        migrations.AlterField(
            model_name='teamrank',
            name='tournament_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rank', to='app.tournament'),
        ),
    ]
