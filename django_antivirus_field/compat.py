# -*- coding: utf-8 -*-

from sys import argv
from django.utils.functional import cached_property as django_cached_property


class cached_property(django_cached_property):

    def __get__(self, instance, type=None):
        if 'test' in argv:
            if instance is None:
                return self

            return self.func(instance)

        return super(cached_property, self).__get__(instance, type)
