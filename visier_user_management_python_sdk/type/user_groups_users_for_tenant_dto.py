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

from visier_user_management_python_sdk.type.simple_user_dto import SimpleUserDTO

class RequiredUserGroupsUsersForTenantDTO(TypedDict):
    pass

class OptionalUserGroupsUsersForTenantDTO(TypedDict, total=False):
    # The unique identifier associated with the tenant.
    tenantCode: str

    # A list of objects representing the users in the user group.
    users: typing.List[SimpleUserDTO]

class UserGroupsUsersForTenantDTO(RequiredUserGroupsUsersForTenantDTO, OptionalUserGroupsUsersForTenantDTO):
    pass
