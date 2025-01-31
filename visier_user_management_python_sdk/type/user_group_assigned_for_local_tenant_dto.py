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


class RequiredUserGroupAssignedForLocalTenantDTO(TypedDict):
    pass

class OptionalUserGroupAssignedForLocalTenantDTO(TypedDict, total=False):
    # The user group ID.
    userGroupId: str

    # An identifiable user group name to display in Visier, such as \"Leadership User Group\".
    displayName: str

class UserGroupAssignedForLocalTenantDTO(RequiredUserGroupAssignedForLocalTenantDTO, OptionalUserGroupAssignedForLocalTenantDTO):
    pass
