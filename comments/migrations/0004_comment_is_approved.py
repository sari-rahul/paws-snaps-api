# Generated by Django 5.0.5 on 2024-05-20 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_remove_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
    ]
