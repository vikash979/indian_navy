# Generated by Django 3.0.7 on 2020-07-20 19:34

import acknowledge.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acknowledge', '0010_auto_20200720_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ack_guidelinesname',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='guidelines/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.newvalidate_image]),
        ),
        migrations.AlterField(
            model_name='ack_publicationname',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='publicattion/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'JPEG', 'pdf', 'PDF'])]),
        ),
    ]
