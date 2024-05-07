# Generated by Django 3.2.25 on 2024-05-07 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, choices=[('dogs', 'Dogs'), ('cats', 'Cats'), ('fishes', 'Fishes'), ('birds', 'Birds'), ('horses', 'Horses'), ('training', 'Training'), ('wellness', 'Wellness'), ('adoption', 'Adoption'), ('other', 'Other')], default=None, max_length=250, null=True),
        ),
    ]
