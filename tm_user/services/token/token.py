#! /usr/bin/python
# Copyright (C) 2025 Paradox
# Release: v2.5.2
# @link olivia.paradox.ai

__author__ = "duc.nguyen"
__date__ = "21/6/25 19:33"

from authtools.models import User
from tm_user.constants.token import TokenKey
from tm_user.services.token.base import BaseToken


class TokenService:

    @classmethod
    def create_token(cls, request, user: User, club_id: int):
        payload = {
            TokenKey.USER_ID: user.id,
            TokenKey.CLUB_ID: club_id,
        }
        jwt_token = BaseToken.encode(payload=payload)

        return jwt_token
