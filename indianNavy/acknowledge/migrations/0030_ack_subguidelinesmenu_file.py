# Generated by Django 2.2.5 on 2020-05-11 16:24

import acknowledge.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acknowledge', '0029_auto_20200511_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='ack_subguidelinesmenu',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='publication/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.validate_image]),
        ),
    ]
