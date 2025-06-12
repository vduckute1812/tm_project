#! /usr/bin/python
# Copyright (C) 2025 Paradox
# Release: v2.5.2
# @link olivia.paradox.ai

__author__ = "duc.nguyen"
__date__ = "5/6/25 19:30"

from rest_framework import status
from rest_framework.response import Response

from tm_club.serializers.club import ClubSerializer
from tm_club.services.club import ClubService
from tm_utils.mixins.view import GenericViewMixin


class ClubView(GenericViewMixin):
    # TODO: user_id = Utils.get_user_id(request) -> Need to build a method to get user_id from request
    #  this user_id should belong to the club, otherwise return 403 Forbidden.

    serializer_class = ClubSerializer

    def list(self, request):
        """
        Get list of all clubs.
        This method should be implemented to return a list of clubs.
        :param request: The HTTP request object.
        :type request: HttpRequest
        :limit: The maximum number of clubs to return (0 for no limit).
        :offset: The number of clubs to skip before starting to collect the result set.
        :return: A response containing the list of clubs.
        """
        data = request.query_params.copy()
        limit = int(data.get("limit", 0))
        offset = int(data.get("offset", 0))
        division_id = int(data.get("division_id", 0))
        clubs = ClubService.get_clubs(division_id, limit, offset)
        data = self.serializer_class(clubs, many=True).data
        return self.response(data=data, status=200, message="Clubs retrieved successfully.")

    def retrieve(self, request, pk):
        """
        Get a specific club by its primary key.
        :param request: The HTTP request object.
        :type request: HttpRequest
        :param pk: The primary key of the club to retrieve.
        :return: A response containing the club data if found, otherwise an error message.
        """
        # user_id = Utils.get_user_id(request)  # TODO: Implement a method to get user_id from request
        if club := ClubService.get(pk):
            data = self.serializer_class(club).data
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
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk: int):
        # user_id = Utils.get_user_id(request)  # TODO: Implement a method to get user_id from request
        data = request.data.copy()
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
