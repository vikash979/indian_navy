# Generated by Django 2.2.5 on 2020-06-03 06:45

import acknowledge.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acknowledge', '0057_auto_20200517_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='brsmenu',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='brsfiles/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.validate_image]),
        ),
        migrations.AddField(
            model_name='brsmenu',
            name='folder_title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brsmenu',
            name='folder_type',
            field=models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=2),
        ),
        migrations.AddField(
            model_name='brsmenu',
            name='menu_type',
            field=models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=1),
        ),
        migrations.AddField(
            model_name='brsmenu',
            name='navyinstructionfile',
            field=models.FileField(blank=True, null=True, upload_to='brsfoldermenus/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.validate_image]),
        ),
        migrations.AddField(
            model_name='brsmenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.BRsmenu'),
        ),
    ]
