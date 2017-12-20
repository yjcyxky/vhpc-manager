import logging
import re
import datetime
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator
from sscobweb.models import (Channel, Package)

logger = logging.getLogger(__name__)

def check_channel_path(channel_path):
    scheme_dict = {
        "http": r"^https?:/{2}\w.+$",
        "ftp": r"^ftp:/{2}\w.+$",
        "file": r"^file:/{3}\w.+$"
    }
    for (key, pattern) in scheme_dict.items():
        if re.match(pattern, channel_path):
            return True
        else:
            return False


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    md5sum = serializers.CharField(max_length = 32, allow_null = True, read_only = True)
    channel_uuid = serializers.UUIDField(format = 'hex_verbose', read_only = True)

    class Meta:
        model = Channel
        fields = ('channel_uuid', 'channel_name', 'arch', 'platform', 'channel_path',
                  'md5sum', 'created_time', 'updated_time', 'is_active', 'summary',
                  'priority_level', 'is_alive', 'total_pkgs_num')
        lookup_field = 'channel_uuid'

    def validate_channel_path(self, channel_path):
        """
        Check that the channel path is valid
        """
        channel_path_lst = channel_path.split('/')
        if 'repodata.json' in channel_path_lst or 'repodata' in channel_path_lst:
            raise serializers.ValidationError("Not valid channel path, Don't contain repodata/repodata.json.")
        if not check_channel_path(channel_path):
            raise serializers.ValidationError("Not valid channel path. Only support http/https/ftp/file")

    def create(self, validated_data):
        channel = Channel.objects.create(**validated_data)
        channel.save()
        return channel

    def update(self, instance, validated_data):
        instance.updated_time = validated_data.get('updated_time', instance.updated_time)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_alive = validated_data.get('is_alive', instance.is_alive)
        instance.priority_level = validated_data.get('priority_level', instance.priority_level)
        instance.channel_path = validated_data.get('channel_path', instance.channel_path)
        instance.md5sum = validated_data.get('md5sum', instance.md5sum)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.channel_name = validated_data.get('channel_name', instance.channel_name)
        instance.total_pkgs_num = validated_data.get('total_pkgs_num', instance.total_pkgs_num)
        instance.save()
        return instance

class PackageSerializer(serializers.HyperlinkedModelSerializer):
    """
    所有Channel添加时都必须与已有的Channel的repodata.json比对，确保不重复添加;
    但已经存在的package可更新channels字段，以保障同一个package可有多个channel与之对应，
    安装时可指定最优的channel来安装相应的package
    """
    pkg_uuid = serializers.UUIDField(format = 'hex_verbose', read_only = True)
    channels = ChannelSerializer(many = True, read_only = True)
    channels_uuid = serializers.PrimaryKeyRelatedField(many=True,
                                                       queryset = Channel.objects.all(),
                                                       pk_field = serializers.UUIDField(format='hex_verbose'),
                                                       source = 'channels')

    class Meta:
        model = Package
        fields = ('pkg_uuid', 'name', 'pkg_name', 'md5sum', 'build', 'build_number',
                  'created_date', 'installed_time', 'license', 'license_family',
                  'size', 'version', 'summary', 'url', 'refereces', 'is_workflow',
                  'is_cluster_pkg', 'created_author', 'frontend_templ', 'output_templ',
                  'report_templ', 'spider_templ', 'module_templ', 'is_installed',
                  'depends', 'first_channel', 'env_name', 'channels', 'channels_uuid')
        lookup_field = 'pkg_uuid'

    def create(self, validated_data):
        package = Package.objects.create(**validated_data)
        package.save()
        channels = validated_data.pop('channels')
        package.channels.add(*channels)
        return package

    def update(self, instance, validated_data):
        instance.is_installed = validated_data.get('is_installed', instance.is_installed)
        channels = validated_data.get('channels', None)
        instance.save()
        if channels:
            instance.channels.clear()
            instance.channels.add(*channels)
        return instance
