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

from visier_user_management_python_sdk.pydantic.simple_user_dto import SimpleUserDTO

class UserGroupsUsersForTenantDTO(BaseModel):
    # The unique identifier associated with the tenant.
    tenant_code: typing.Optional[str] = Field(None, alias='tenantCode')

    # A list of objects representing the users in the user group.
    users: typing.Optional[typing.List[SimpleUserDTO]] = Field(None, alias='users')
    class Config:
        arbitrary_types_allowed = True
