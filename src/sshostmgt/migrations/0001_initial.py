# Generated by Django 3.0.5 on 2020-04-12 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BIOS',
            fields=[
                ('bios_uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('host_uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('hostname', models.CharField(max_length=64, unique=True)),
                ('host_desc', models.CharField(max_length=255, null=True)),
                ('mgmt_ip_addr', models.CharField(max_length=16, unique=True)),
                ('mgmt_mac', models.CharField(max_length=17, unique=True)),
                ('cluster_uuid', models.CharField(max_length=128, null=True)),
            ],
            options={
                'ordering': ('hostname',),
            },
        ),
        migrations.CreateModel(
            name='IPMI',
            fields=[
                ('ipmi_uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('ipmi_mac', models.CharField(max_length=17, unique=True)),
                ('ipmi_addr', models.CharField(max_length=15, unique=True)),
                ('ipmi_username', models.CharField(default='root', max_length=32)),
                ('ipmi_passwd', models.CharField(default='calvin', max_length=32)),
                ('ipmi_desc', models.CharField(max_length=255, null=True)),
                ('power_state', models.CharField(choices=[('power_on', 'POWER_ON'), ('power_off', 'POWER_OFF'), ('reboot', 'REBOOT'), ('unknown', 'UNKNOWN'), ('changed', 'CHANGED'), ('POWER_ON', 'POWER_ON'), ('POWER_OFF', 'POWER_OFF'), ('REBOOT', 'REBOOT'), ('UNKNOWN', 'UNKNOWN'), ('CHANGED', 'CHANGED')], default='POWER_OFF', max_length=10)),
                ('last_update_time', models.DateTimeField()),
                ('first_add_time', models.DateTimeField()),
            ],
            options={
                'ordering': ('ipmi_addr',),
            },
        ),
        migrations.CreateModel(
            name='RAID',
            fields=[
                ('raid_uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('system_uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('tag_name_alias', models.CharField(max_length=32, null=True)),
                ('tag_name', models.CharField(max_length=32, unique=True)),
                ('tag_desc', models.CharField(max_length=255, null=True)),
                ('label_color', models.CharField(default='#23d7bc', max_length=32)),
                ('common_used', models.BooleanField()),
            ],
            options={
                'ordering': ('tag_name',),
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('storage_uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('storage_name', models.CharField(max_length=128, unique=True)),
                ('storage_path', models.CharField(max_length=255, unique=True)),
                ('storage_desc', models.CharField(max_length=255, null=True)),
                ('total_size', models.PositiveIntegerField()),
                ('remaining_size', models.PositiveIntegerField()),
                ('username', models.CharField(max_length=16)),
                ('groupname', models.CharField(max_length=16)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sshostmgt.Host')),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('network_uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('network_name', models.CharField(max_length=128, unique=True)),
                ('mac_addr', models.CharField(max_length=17, unique=True)),
                ('ip_addr', models.CharField(max_length=16, unique=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sshostmgt.Host')),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('memory_uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sshostmgt.Host')),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='ipmi',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sshostmgt.IPMI'),
        ),
        migrations.AddField(
            model_name='host',
            name='tags',
            field=models.ManyToManyField(to='sshostmgt.Tag'),
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('cpu_uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sshostmgt.Host')),
            ],
        ),
    ]
