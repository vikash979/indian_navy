# Generated by Django 2.2.5 on 2020-04-26 16:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('acknowledge', '0002_auto_20200426_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='ack_policyname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('policy_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='acknoledge_menu',
            name='parent',
        ),
        migrations.CreateModel(
            name='Comment_policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.CharField(max_length=50)),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='policy/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF'])])),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ack_submenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_submenues', to='acknowledge.acknoledge_menu')),
            ],
        ),
    ]
