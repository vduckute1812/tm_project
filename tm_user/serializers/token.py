#! /usr/bin/python
# Copyright (C) 2025 Paradox
# Release: v2.5.2
# @link olivia.paradox.ai

__author__ = "duc.nguyen"
__date__ = "21/6/25 19:15"

from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    club_id = serializers.IntegerField(required=True)
    expired_at = serializers.IntegerField(required=True)
    user_id = serializers.IntegerField(required=True)
