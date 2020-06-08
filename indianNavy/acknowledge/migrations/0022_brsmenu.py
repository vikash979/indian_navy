# Generated by Django 2.2.5 on 2020-05-07 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acknowledge', '0021_auto_20200507_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='BRsmenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200, unique=True)),
                ('parent', models.ForeignKey(blank=True, limit_choices_to={'id': 16}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brsmenues', to='acknowledge.acknoledge_menu')),
            ],
        ),
    ]
