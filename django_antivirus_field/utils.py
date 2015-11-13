# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import warnings
from django_antivirus_field import settings

_clam = None


def get_clam():
    if not settings.antivirus_on:
        return None

    global _clam

    if _clam is None:
        try:
            import pyclamd

            if settings.clam_socktype == 'unix':
                _clam = pyclamd.ClamdUnixSocket()

            elif settings.clam_socktype == 'tcp':
                _clam = pyclamd.ClamdNetworkSocket(host=settings.clam_host, port=settings.clam_port)

            _clam.ping()

        except Exception as err:
            warnings.warn('Problem with ClamAV: {}'.format(str(err)))
            _clam = None

    return _clam


def is_infected(stream):
    """
    Create tmp file and scan it with ClamAV
    Returns
        True, 'Virus name' - if virus detected
        False, '' - if not virus detected
        None, '' - status unknown (pyclamd not installed)
    """
    clam = get_clam()
    if not settings.antivirus_on or clam is None:
        return None, ''

    result = clam.scan_stream(stream)
    if result:
        return True, result['stream']

    return False, ''
