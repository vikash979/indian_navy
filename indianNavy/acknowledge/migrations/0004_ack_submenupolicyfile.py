# Generated by Django 3.0.7 on 2020-07-17 12:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acknowledge', '0003_auto_20200714_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='ack_subMenuPolicyFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200)),
                ('folder_title', models.CharField(max_length=200)),
                ('file', models.FileField(blank=True, null=True, upload_to='policy/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF'])])),
                ('parent_ob', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ack_submenu_children', to='acknowledge.ack_submenu')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
