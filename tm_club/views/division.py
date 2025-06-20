#! /usr/bin/python
# Copyright (C) 2025 Paradox
# Release: v2.5.2
# @link olivia.paradox.ai

__author__ = "duc.nguyen"
__date__ = "5/6/25 19:30"

from rest_framework import status
from rest_framework.response import Response

from tm_club.serializers.division import DivisionSerializer
from tm_club.services.division import DivisionService
from tm_utils.mixins.view import GenericViewMixin


class DivisionView(GenericViewMixin):
    # TODO: user_id = Utils.get_user_id(request) -> Need to build a method to get user_id from request
    #  this user_id should belong to the club, otherwise return 403 Forbidden.

    serializer_class = DivisionSerializer

    def retrieve(self, request, pk):
        if division := DivisionService.get(pk):
            data = self.serializer_class(division).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """
        Create a new club.
        This method should be implemented to create a new club.
        :param request: The HTTP request object containing club data.
        :type request: HttpRequest
        :return: A response indicating the success or failure of the club creation.
        """
        # user_id = Utils.get_user_id(request)  # TODO: Implement a method to get user_id from request
        data = request.data.copy()
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk: int):
        # user_id = Utils.get_user_id(request)  # TODO: Implement a method to get user_id from request
        data = request.data.copy()
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
