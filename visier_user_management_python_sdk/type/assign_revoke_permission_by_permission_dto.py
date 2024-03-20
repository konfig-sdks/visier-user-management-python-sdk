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

from visier_user_management_python_sdk.type.assign_revoke_permission_by_user_dto import AssignRevokePermissionByUserDTO
from visier_user_management_python_sdk.type.permission_assigned_for_local_tenant_dto import PermissionAssignedForLocalTenantDTO

class RequiredAssignRevokePermissionByPermissionDTO(TypedDict):
    pass

class OptionalAssignRevokePermissionByPermissionDTO(TypedDict, total=False):
    permission: PermissionAssignedForLocalTenantDTO

    # A list of objects representing the users that was permission was assigned to or removed from.
    users: typing.List[AssignRevokePermissionByUserDTO]

class AssignRevokePermissionByPermissionDTO(RequiredAssignRevokePermissionByPermissionDTO, OptionalAssignRevokePermissionByPermissionDTO):
    pass
