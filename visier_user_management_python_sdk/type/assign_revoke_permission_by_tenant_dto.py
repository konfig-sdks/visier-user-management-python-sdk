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

from visier_user_management_python_sdk.type.assign_revoke_permission_by_permission_dto import AssignRevokePermissionByPermissionDTO

class RequiredAssignRevokePermissionByTenantDTO(TypedDict):
    pass

class OptionalAssignRevokePermissionByTenantDTO(TypedDict, total=False):
    # The unique identifier associated with the tenant.
    tenantCode: str

    # A list of objects representing the assigned or removed permissions.
    permissions: typing.List[AssignRevokePermissionByPermissionDTO]

    # The state of the permission assignment. Valid values are Succeed or Failed.
    status: str

    # A detailed description of the request outcome, if available.
    message: str

class AssignRevokePermissionByTenantDTO(RequiredAssignRevokePermissionByTenantDTO, OptionalAssignRevokePermissionByTenantDTO):
    pass
