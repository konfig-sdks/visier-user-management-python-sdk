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


class PermissionAssignedUserDTO(BaseModel):
    # The unique identifier associated with the user.
    user_id: typing.Optional[str] = Field(None, alias='userId')

    # The user's username. This is typically the user's email, such as john@visier.com.
    username: typing.Optional[str] = Field(None, alias='username')

    # The method through which the user was assigned the permission. The permission may be assigned through  the following options:   - User: The permission was directly assigned to the user.   - UserGroup: The permission was assigned because the user belongs to a user group that is assigned the permission.   - UserAndUserGroup: The permission was directly assigned to the user and assigned because the user belongs to     a user group that is assigned the permission.
    permission_from: typing.Optional[str] = Field(None, alias='permissionFrom')
    class Config:
        arbitrary_types_allowed = True
