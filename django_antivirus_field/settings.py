# -*- coding: utf-8 -*-

import sys
from django.conf import settings

from django_antivirus_field.compat import cached_property


class Settings(object):

    @cached_property
    def antivirus_on(self):
        return getattr(settings, 'CLAMAV_ACTIVE', False)

    @cached_property
    def clam_socktype(self):
        return getattr(settings, 'CLAMAV_SOCKTYPE', 'unix')

    @cached_property
    def clam_host(self):
        return getattr(settings, 'CLAMAV_HOST', 'localhost')

    @cached_property
    def clam_port(self):
        return getattr(settings, 'CLAMAV_PORT', 3310)

    @cached_property
    def clam_fail_cascade(self):
        return getattr(settings, 'CLAMAV_FAIL_CASCADE', False)


sys.modules[__name__] = Settings()
