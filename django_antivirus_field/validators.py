# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django_antivirus_field.utils import is_infected


def file_validator(f):
    has_virus, name = is_infected(f.file.read())
    if has_virus:
        raise ValidationError(_('Virus "{}" was detected').format(name))

