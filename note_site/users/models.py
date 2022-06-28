from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name=_("user"),
    )
    picture = models.ImageField(
        _("picture"), upload_to="user_profile/img", null=True, blank=True
    )

    def __str__(self):
        return str(self.user)
