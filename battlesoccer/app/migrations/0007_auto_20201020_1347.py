# Generated by Django 2.1.7 on 2020-10-20 08:17

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201020_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimage',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=0, size=[500, 500], upload_to=''),
        ),
    ]
