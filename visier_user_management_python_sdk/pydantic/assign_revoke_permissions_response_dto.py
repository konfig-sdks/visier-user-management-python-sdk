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
from pydantic import BaseModel, Field, RootModel

from visier_user_management_python_sdk.pydantic.assign_revoke_permission_by_tenant_dto import AssignRevokePermissionByTenantDTO

class AssignRevokePermissionsResponseDTO(BaseModel):
    # A list of objects representing the users that were assigned permissions, organized by the tenants the users belong to.
    tenants: typing.Optional[typing.List[AssignRevokePermissionByTenantDTO]] = Field(None, alias='tenants')
    class Config:
        arbitrary_types_allowed = True
