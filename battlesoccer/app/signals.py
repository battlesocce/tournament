from django.db.models.signals import post_save
from django.dispatch import receiver
from app.models import team
from users.models import CustomUser
from django.conf import settings
from core.utils import generate_random_string
from django.db.models.signals import pre_save
from django.utils.text import slugify


@receiver(post_save, sender=CustomUser)
def create_team(sender, instance ,created, **kwargs):
    if created and instance.id:
        userdetail=CustomUser.objects.get(pk=instance.id)
        if  userdetail.is_team:
            team.objects.create(id=instance.id,user=instance,teamname=instance)
        
        