# Generated by Django 2.2.5 on 2020-05-14 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acknowledge', '0041_ack_submenu_parent_ob'),
    ]

    operations = [
        migrations.AddField(
            model_name='ack_submenu',
            name='folder_title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ack_submenu',
            name='folder_type',
            field=models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=2),
        ),
        migrations.AddField(
            model_name='ack_submenu',
            name='menu_type',
            field=models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=1),
        ),
        migrations.AddField(
            model_name='ack_submenu',
            name='older_type',
            field=models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=2),
        ),
    ]