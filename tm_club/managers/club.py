#! /usr/bin/python
# Copyright (C) 2025 Paradox
# Release: v2.5.2
# @link olivia.paradox.ai

__author__ = "duc.nguyen"
__date__ = "5/6/25 19:37"

from tm_utils.managers.base import BaseManager, BaseQuerySet

class ClubQuerySet(BaseQuerySet):
    def belong_to_division(self, division_id: int):
        return self.filter(division_id=division_id)

class ClubManager(BaseManager):
    def get_queryset(self):
        return ClubQuerySet(self.model, using=self._db)
