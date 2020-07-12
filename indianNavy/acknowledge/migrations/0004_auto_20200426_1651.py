# Generated by Django 2.2.5 on 2020-04-26 16:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acknowledge', '0003_auto_20200426_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='ack_policypolicyfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='policy/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF'])])),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('parent_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_policyfile', to='acknowledge.ack_policyname')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Comment_policy',
        ),
    ]