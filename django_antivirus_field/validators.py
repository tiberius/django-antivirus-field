# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyclamd import ConnectionError

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django_antivirus_field.utils import is_infected

from django_antivirus_field import settings


class ClamError(Exception):
    pass


class VirusError(ValidationError):
    pass

_virus_check_fail_msg = _('Virus checking failed')


def file_validator(f):
    try:

        has_virus, name = is_infected(f.file.read())

    except ConnectionError:
        raise ClamError(_virus_check_fail_msg)

    if has_virus is None and settings.clam_fail_cascade:
        raise ClamError(_virus_check_fail_msg)

    if has_virus:
        raise VirusError(_('Virus "%(name)s" was detected'), params={'name': name}, code='virus')
