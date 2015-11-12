# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django_antivirus_field.utils import is_infected

from django.conf import settings
CLAMAV_FAIL_CASCADE = getattr(settings, 'CLAMAV_FAIL_CASCADE', False)


def file_validator(f):
    has_virus, name = is_infected(f.file.read())

    if has_virus is None and CLAMAV_FAIL_CASCADE:
        raise ValidationError(_('Virus checking failed'))

    if has_virus:
        raise ValidationError(_('Virus "%(name)s" was detected'), params={'name': name})
