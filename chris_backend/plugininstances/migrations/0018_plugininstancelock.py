# Generated by Django 2.2.12 on 2020-12-16 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plugininstances', '0017_auto_20201203_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='PluginInstanceLock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plugin_inst', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lock', to='plugininstances.PluginInstance')),
            ],
        ),
    ]
