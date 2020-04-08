# Generated by Django 3.0.5 on 2020-04-08 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sshostmgt', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='host',
            options={'ordering': ('hostname',)},
        ),
        migrations.AlterModelOptions(
            name='ipmi',
            options={'ordering': ('ipmi_addr',)},
        ),
        migrations.AlterModelOptions(
            name='memory',
            options={},
        ),
        migrations.AlterModelOptions(
            name='network',
            options={},
        ),
        migrations.AlterModelOptions(
            name='storage',
            options={},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('tag_name',)},
        ),
    ]