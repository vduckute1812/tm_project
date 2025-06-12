#! /usr/bin/python
# Copyright (C) 2025 Paradox
# Release: v2.5.2
# @link olivia.paradox.ai

__author__ = "duc.nguyen"
__date__ = "5/6/25 19:39"

from django.db.models import Manager, QuerySet

class BaseQuerySet(QuerySet):
    # TODO: Implement the BaseQuerySet class with necessary methods and properties
    pass

class BaseManager(Manager):
    # TODO: Implement the BaseManager class with necessary methods and properties

    def get_queryset(self):
        return BaseQuerySet(self.model, using=self._db)

