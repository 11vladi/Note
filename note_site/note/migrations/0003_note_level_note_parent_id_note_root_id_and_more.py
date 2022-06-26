# Generated by Django 4.0.5 on 2022-06-07 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_alter_note_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='note',
            name='parent_id',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='note',
            name='root_id',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.DeleteModel(
            name='NotesTree',
        ),
    ]