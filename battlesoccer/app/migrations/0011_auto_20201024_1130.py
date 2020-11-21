# Generated by Django 2.1.7 on 2020-10-24 06:00

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_totalteamrank'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='tour_coverpic',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=100, size=[800, 200], upload_to=''),
        ),
        migrations.AddField(
            model_name='tournament',
            name='tour_defender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='defender', to='app.player'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='tour_goalkeaper',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='goalkeaper', to='app.player'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='tour_highgoals',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='highgoals', to='app.player'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='tour_moves',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='moves', to='app.player'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='tour_player',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bestplayer', to='app.player'),
        ),
    ]