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

from visier_user_management_python_sdk.type.permission_assigned_user_dto import PermissionAssignedUserDTO

class RequiredPermissionAssignedByTenantDTO(TypedDict):
    pass

class OptionalPermissionAssignedByTenantDTO(TypedDict, total=False):
    # The unique identifier associated with the tenant.
    tenantCode: str

    # A list of objects representing the users that the permission is assigned to.
    users: typing.List[PermissionAssignedUserDTO]

class PermissionAssignedByTenantDTO(RequiredPermissionAssignedByTenantDTO, OptionalPermissionAssignedByTenantDTO):
    pass
