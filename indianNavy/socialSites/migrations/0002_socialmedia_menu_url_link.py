# Generated by Django 2.2.5 on 2020-04-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialSites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia_menu',
            name='url_link',
            field=models.URLField(blank=True),
        ),
    ]