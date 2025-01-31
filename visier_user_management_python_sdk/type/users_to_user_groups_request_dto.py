# coding: utf-8

"""
    Visier User Management APIs

    Visier APIs for managing users within an organization

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from visier_user_management_python_sdk.type.users_to_user_group_request_dto import UsersToUserGroupRequestDTO

class RequiredUsersToUserGroupsRequestDTO(TypedDict):
    pass

class OptionalUsersToUserGroupsRequestDTO(TypedDict, total=False):
    # A list of objects representing the user groups and users to assign or remove.
    userGroups: typing.List[UsersToUserGroupRequestDTO]

class UsersToUserGroupsRequestDTO(RequiredUsersToUserGroupsRequestDTO, OptionalUsersToUserGroupsRequestDTO):
    pass
