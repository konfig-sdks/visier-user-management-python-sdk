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

from visier_user_management_python_sdk.pydantic.permissions_to_user_group_request_dto_permissions_ids import PermissionsToUserGroupRequestDTOPermissionsIds

class PermissionsToUserGroupRequestDTO(BaseModel):
    # The unique identifier associated with the user group.
    user_group_id: typing.Optional[str] = Field(None, alias='userGroupId')

    permissions_ids: typing.Optional[PermissionsToUserGroupRequestDTOPermissionsIds] = Field(None, alias='permissionsIds')
    class Config:
        arbitrary_types_allowed = True
