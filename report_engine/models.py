# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django_mysql import models as mysql_models
import uuid
import os

from django.conf import settings

USER_HOME = os.path.expanduser("~")

def get_report_engine_home(create_flag = False):
    DEFAULT_HOME = os.path.join(USER_HOME, 'report_engine')
    REPORT_ENGINE_HOME = getattr(settings, 'REPORT_ENGINE_HOME', DEFAULT_HOME)
    if create_flag:
        os.makedirs(REPORT_ENGINE_HOME)
    return REPORT_ENGINE_HOME

class TitleNode(models.Model):
    title_uuid = models.CharField(max_length = 36, primary_key = True,
                                  default = uuid.uuid4())
    created_time = models.DateTimeField(auto_now_add=True)
    content = mysql_models.JSONField(max_length = 255)

    def __str__(self):
        return '%s' % self.title_uuid

    class Meta:
        ordering = ('created_time', )
        permissions = (("list_title", "can list title instance(s)"),)


class InfoNode(models.Model):
    info_uuid = models.CharField(max_length = 36, primary_key = True,
                                 default = uuid.uuid4())
    created_time = models.DateTimeField(auto_now_add=True)
    content = mysql_models.JSONField(max_length = 255)

    def __str__(self):
        return '%s' % self.info_uuid

    class Meta:
        ordering = ('created_time', )
        permissions = (("list_info", "can list info instance(s)"),)


class ParagraphNode(models.Model):
    paragraph_uuid = models.CharField(max_length = 36, primary_key = True,
                                      default = uuid.uuid4())
    created_time = models.DateTimeField(auto_now_add=True)
    content = mysql_models.JSONField(max_length = 255)

    def __str__(self):
        return '%s' % self.paragraph_uuid

    class Meta:
        ordering = ('created_time', )
        permissions = (("list_paragraph", "can list paragraph instance(s)"),)


class MediaNode(models.Model):
    media_uuid = models.CharField(max_length = 36, primary_key = True,
                                  default = uuid.uuid4())
    created_time = models.DateTimeField(auto_now_add=True)
    content = mysql_models.JSONField(max_length = 255)

    def __str__(self):
        return '%s' % self.media_uuid

    class Meta:
        ordering = ('created_time', )
        permissions = (("list_media", "can list media instance(s)"),)


class UrlNode(models.Model):
    url_uuid = models.CharField(max_length = 36, primary_key = True,
                                default = uuid.uuid4())
    created_time = models.DateTimeField(auto_now_add=True)
    content = mysql_models.JSONField(max_length = 255)

    def __str__(self):
        return '%s' % self.url_uuid

    class Meta:
        ordering = ('created_time', )
        permissions = (("list_url", "can list url instance(s)"),)


class ReferenceNode(models.Model):
    reference_uuid = models.CharField(max_length = 36, primary_key = True,
                                      default = uuid.uuid4())
    created_time = models.DateTimeField(auto_now_add=True)
    content = mysql_models.JSONField(max_length = 255)

    def __str__(self):
        return '%s' % self.reference_uuid

    class Meta:
        ordering = ('created_time', )
        permissions = (("list_reference", "can list reference instance(s)"),)


class HeaderNode(models.Model):
    header_uuid = models.CharField(max_length = 36, primary_key = True,
                                   default = uuid.uuid4())
    created_time = models.DateTimeField(auto_now_add=True)
    content = mysql_models.JSONField(max_length = 255)

    def __str__(self):
        return '%s' % self.header_uuid

    class Meta:
        ordering = ('created_time', )
        permissions = (("list_header", "can list header instance(s)"),)


class FooterNode(models.Model):
    footer_uuid = models.CharField(max_length = 36, primary_key = True,
                                   default = uuid.uuid4())
    created_time = models.DateTimeField(auto_now_add=True)
    content = mysql_models.JSONField(max_length = 255)

    def __str__(self):
        return '%s' % self.footer_uuid

    class Meta:
        ordering = ('created_time', )
        permissions = (("list_footer", "can list footer instance(s)"),)


class ListNode(models.Model):
    list_uuid = models.CharField(max_length = 36, primary_key = True,
                                 default = uuid.uuid4())
    created_time = models.DateTimeField(auto_now_add=True)
    content = mysql_models.JSONField(max_length = 255)

    def __str__(self):
        return '%s' % self.list_uuid

    class Meta:
        ordering = ('created_time', )
        permissions = (("list_list", "can list list instance(s)"),)


class TableNode(models.Model):
    table_uuid = models.CharField(max_length = 36, primary_key = True,
                                  default = uuid.uuid4())
    created_time = models.DateTimeField(auto_now_add=True)
    content = mysql_models.JSONField(max_length = 255)

    def __str__(self):
        return '%s' % self.table_uuid

    class Meta:
        ordering = ('created_time', )
        permissions = (("list_table", "can list table instance(s)"),)


class Version(models.Model):
    version_uuid = models.CharField(max_length = 36, primary_key = True,
                                    default = uuid.uuid4())
    created_time = models.DateTimeField(auto_now_add=True)
    name_alias = models.CharField(max_length = 32)

    def __str__(self):
        return '%s' % self.version_uuid

    class Meta:
        ordering = ('created_time', )
        permissions = (("list_version", "can list version instance(s)"),)


class ReportNode(models.Model):
    report_uuid = models.CharField(max_length = 36, primary_key = True,
                                   default = uuid.uuid4())
    latest = models.CharField(max_length = 36, unique = True,
                              default = uuid.uuid4())
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(null = True)
    patient = models.CharField(max_length = 36, default = uuid.uuid4())
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    version_set = models.ManyToManyField(Version)


class SectionNode(models.Model):
    TYPES = (
        ('ROOT', 'ROOT'),
        ('root', 'ROOT'),
        ('SECTION', 'SECTION'),
        ('section', 'SECTION'),
    )
    section_uuid = models.CharField(max_length = 36, primary_key = True,
                                    default = uuid.uuid4())
    created_time = models.DateTimeField(auto_now_add=True)
    # updated_time = models.DateTimeField(null = True)
    node_type = models.CharField(max_length = 32, choices = TYPES)
    json_path = models.CharField(max_length = 255)
    title_node = models.OneToOneField(TitleNode, null=True, on_delete = models.CASCADE)
    info_node = models.OneToOneField(InfoNode, null=True, on_delete = models.CASCADE)
    paragraph_node = models.OneToOneField(ParagraphNode, null=True, on_delete = models.CASCADE)
    media_node = models.OneToOneField(MediaNode, null=True, on_delete = models.CASCADE)
    url_node = models.OneToOneField(UrlNode, null=True, on_delete = models.CASCADE)
    reference_node = models.OneToOneField(ReferenceNode, null=True, on_delete = models.CASCADE)
    header_node = models.OneToOneField(HeaderNode, null=True, on_delete = models.CASCADE)
    footer_node = models.OneToOneField(FooterNode, null=True, on_delete = models.CASCADE)
    list_node = models.OneToOneField(ListNode, null=True, on_delete = models.CASCADE)
    table_node = models.OneToOneField(TableNode, null=True, on_delete = models.CASCADE)
    section_node = models.ForeignKey('self', null=True, on_delete = models.CASCADE)
    report = models.ForeignKey(ReportNode, null = True, blank = True,
                               related_name = 'root_node_set',
                               on_delete = models.CASCADE)

    def __str__(self):
        return '%s' % self.section_uuid

    class Meta:
        ordering = ('created_time', )
        permissions = (("list_section", "can list section instance(s)"),)
