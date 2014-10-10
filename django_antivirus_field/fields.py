# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django_antivirus_field.validators import file_validator


class ProtectedFileField(models.FileField):
    def __init__(self, *args, **kwargs):
        super(ProtectedFileField, self).__init__(*args, **kwargs)
        self.validators.append(file_validator)
