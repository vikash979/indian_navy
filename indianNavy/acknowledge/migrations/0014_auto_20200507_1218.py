# Generated by Django 2.2.5 on 2020-05-07 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acknowledge', '0013_auto_20200507_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ack_policyname',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 52}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='policy_name', to='acknowledge.ack_submenu'),
        ),
    ]