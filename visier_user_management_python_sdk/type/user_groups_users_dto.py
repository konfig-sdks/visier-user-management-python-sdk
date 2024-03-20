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

from visier_user_management_python_sdk.type.user_groups_users_for_tenant_dto import UserGroupsUsersForTenantDTO

class RequiredUserGroupsUsersDTO(TypedDict):
    pass

class OptionalUserGroupsUsersDTO(TypedDict, total=False):
    # A list of objects representing the users that are explicitly assigned to the user group, organized by the tenants the users belong to.
    tenants: typing.List[UserGroupsUsersForTenantDTO]

    # The limit of results to return. The maximum value is 1000.
    limit: int

    # The index to start retrieving values from, also known as offset. The index begins at 0.
    start: int

class UserGroupsUsersDTO(RequiredUserGroupsUsersDTO, OptionalUserGroupsUsersDTO):
    pass
