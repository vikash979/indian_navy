# Generated by Django 2.2.5 on 2020-05-07 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acknowledge', '0017_ack_publicationname'),
    ]

    operations = [
        migrations.CreateModel(
            name='ack_subGuidelinesmenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200, unique=True)),
                ('parent', models.ForeignKey(blank=True, limit_choices_to={'id': 11}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_subguidelinesmenues', to='acknowledge.acknoledge_menu')),
            ],
        ),
    ]