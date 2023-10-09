from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import generate_avatar
from django.core.files.base import ContentFile


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",
                                     related_name="followed_by",
                                     symmetrical=False,
                                     blank=True)

    date_modified = models.DateTimeField(User, auto_now=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images")
    profile_bio = models.CharField(null=True, blank=True, max_length=500)
    homepage_link = models.CharField(null=True, blank=True, max_length=100)
    instagram_link = models.CharField(null=True, blank=True, max_length=100)
    facebook_link = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        avatar_svg = generate_avatar(instance.username)

        user_profile = Profile(user=instance)
        user_profile.profile_image.save(f'{instance.username}_avatar.svg', ContentFile(avatar_svg.encode('utf-8')))

        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()


class Snippet(models.Model):
    user = models.ForeignKey(User, related_name="snippets", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="snippet_like", blank=True)

    # keep count of likes

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.user} " \
               f"{self.created_at:%Y-%m-%d %H:%M}: " \
               f"{self.body}"


class SharedSnippet(models.Model):
    original_snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE, related_name="shared_snippet")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shared by {self.user} at {self.shared_at}"