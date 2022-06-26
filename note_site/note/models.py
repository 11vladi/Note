from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from tinymce import models as tinymce_models


class Note(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT,default=0,)
    parent_id=models.BigIntegerField(default=-1)
    level=models.IntegerField(default=0)
    name = models.CharField(_('Name'), max_length=200)
    text = tinymce_models.HTMLField()

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['user_id', 'level','name']),
        ]



