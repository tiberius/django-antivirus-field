# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import warnings

from django.conf import settings


ANTIVIRUS_ON = getattr(settings, 'CLAMAV_ACTIVE', False)

if ANTIVIRUS_ON:
    try:
        import pyclamd

        clam = pyclamd.ClamdUnixSocket()
        clam.ping()

    except Exception as err:
        warnings.warn('Problem with ClamAV: {}'.format(str(err)))
        clam = None


def is_infected(stream):
    """
    Create tmp file and scan it with ClamAV
    Returns
        True, 'Virus name' - if virus detected
        False, '' - if not virus detected
        None, '' - status unknown (pyclamd not installed)
    """
    if not ANTIVIRUS_ON or clam is None:
        return None, ''

    result = clam.scan_stream(stream)
    if result:
        return True, result['stream']

    return False, ''
