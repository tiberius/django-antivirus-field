# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import warnings

try:
    import django
except ImportError as err:
    warnings.warn('Cannot import django: {}'.format(str(err)))
    sys.exit(1)

from django_antivirus_field.fields import ProtectedFileField

if django.VERSION[1] < 7:  # django < 1.7.0
    try:
        from south.modelsinspector import add_introspection_rules

        add_introspection_rules([], ["^django_antivirus_field\.fields\.ProtectedFileField"])
    except Exception as err:
        warnings.warn('Problem with south: {}'.format(str(err)))

__ALL__ = ['ProtectedFileField']
