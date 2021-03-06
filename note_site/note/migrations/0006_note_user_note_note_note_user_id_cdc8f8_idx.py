# Generated by Django 4.0.5 on 2022-06-17 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("note", "0005_remove_note_root_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="user",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddIndex(
            model_name="note",
            index=models.Index(
                fields=["user_id", "level", "name"], name="note_note_user_id_cdc8f8_idx"
            ),
        ),
    ]
