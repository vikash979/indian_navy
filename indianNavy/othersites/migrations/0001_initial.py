# Generated by Django 2.2.5 on 2020-04-28 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='other_sites_parent_menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('menu_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='other_sites_menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('menu_name', models.CharField(max_length=200, unique=True)),
                ('menu_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=1)),
                ('folder_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=2)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='othersiteParent_menu', to='othersites.other_sites_parent_menu')),
                ('parent_ob', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='othersites.other_sites_menu')),
            ],
        ),
    ]
