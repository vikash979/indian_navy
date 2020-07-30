# Generated by Django 3.0.7 on 2020-07-14 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acknowledge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphdetailuser',
            name='menu_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acknowledge.Country'),
        ),
        migrations.AddField(
            model_name='brsmenu',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 8}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brsmenues', to='acknowledge.acknoledge_menu'),
        ),
        migrations.AddField(
            model_name='brsmenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.BRsmenu'),
        ),
        migrations.AddField(
            model_name='ack_substandardsmenu',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 4}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_substandardsmenues', to='acknowledge.acknoledge_menu'),
        ),
        migrations.AddField(
            model_name='ack_substandardsmenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_subStandardsmenu'),
        ),
        migrations.AddField(
            model_name='ack_subpublicationmenu',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 2}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_subpublicationmenues', to='acknowledge.acknoledge_menu'),
        ),
        migrations.AddField(
            model_name='ack_subpublicationmenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_subpublicationmenu'),
        ),
        migrations.AddField(
            model_name='ack_subnhqe_librarylinesmenu',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 7}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_subnohqsmenues', to='acknowledge.acknoledge_menu'),
        ),
        migrations.AddField(
            model_name='ack_subnhqe_librarylinesmenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_subNHQe_Librarylinesmenu'),
        ),
        migrations.AddField(
            model_name='ack_subnavy_orderssmenu',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 5}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_subnavy_ordersmenues', to='acknowledge.acknoledge_menu'),
        ),
        migrations.AddField(
            model_name='ack_subnavy_orderssmenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_subNavy_Orderssmenu'),
        ),
        migrations.AddField(
            model_name='ack_subnavy_instructionssmenu',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 6}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_subnavy_instructionmenues', to='acknowledge.acknoledge_menu'),
        ),
        migrations.AddField(
            model_name='ack_subnavy_instructionssmenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_subNavy_Instructionssmenu'),
        ),
        migrations.AddField(
            model_name='ack_submenu',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 1}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_submenues', to='acknowledge.acknoledge_menu'),
        ),
        migrations.AddField(
            model_name='ack_submenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='acknowledge.ack_submenu'),
        ),
        migrations.AddField(
            model_name='ack_subguidelinesmenu',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 3}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_subguidelinesmenues', to='acknowledge.acknoledge_menu'),
        ),
        migrations.AddField(
            model_name='ack_subguidelinesmenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_subGuidelinesmenu'),
        ),
        migrations.AddField(
            model_name='ack_standardsname',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='standards_name', to='acknowledge.ack_subStandardsmenu'),
        ),
        migrations.AddField(
            model_name='ack_standardsname',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_Standardsname'),
        ),
        migrations.AddField(
            model_name='ack_publicationname',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='public_name', to='acknowledge.ack_subpublicationmenu'),
        ),
        migrations.AddField(
            model_name='ack_publicationname',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_publicationname'),
        ),
        migrations.AddField(
            model_name='ack_publicationfile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ack_policypolicyfile',
            name='parent_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_policyfile', to='acknowledge.ack_policyname'),
        ),
        migrations.AddField(
            model_name='ack_policypolicyfile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ack_policyname',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='policy_name', to='acknowledge.ack_submenu'),
        ),
        migrations.AddField(
            model_name='ack_policyname',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_policyname'),
        ),
        migrations.AddField(
            model_name='ack_navyname',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='navyOrders_name', to='acknowledge.ack_subNavy_Orderssmenu'),
        ),
        migrations.AddField(
            model_name='ack_navyname',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_Navyname'),
        ),
        migrations.AddField(
            model_name='ack_navyinstructionname',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='navyinstruction_name', to='acknowledge.ack_subNavy_Instructionssmenu'),
        ),
        migrations.AddField(
            model_name='ack_navyinstructionname',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_NavyInstructionname'),
        ),
        migrations.AddField(
            model_name='ack_guidelinesname',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guidelines_name', to='acknowledge.ack_subGuidelinesmenu'),
        ),
        migrations.AddField(
            model_name='ack_guidelinesname',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_guidelinesname'),
        ),
    ]