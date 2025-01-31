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

from visier_user_management_python_sdk.pydantic.permission_assigned_by_tenant_dto import PermissionAssignedByTenantDTO

class PermissionAssignedUsersDTO(BaseModel):
    # A list of objects representing the users that are assigned the specific permission, organized by the tenants the users belong to.
    tenants: typing.Optional[typing.List[PermissionAssignedByTenantDTO]] = Field(None, alias='tenants')

    # The number of results to return. The maximum number of tenants to retrieve is 100.
    limit: typing.Optional[int] = Field(None, alias='limit')

    # The index to start retrieving results from, also known as offset. The index begins at 0.
    start: typing.Optional[int] = Field(None, alias='start')
    class Config:
        arbitrary_types_allowed = True
