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

from visier_user_management_python_sdk.type.permissions_to_user_group_request_dto_permissions_ids import PermissionsToUserGroupRequestDTOPermissionsIds

class RequiredPermissionsToUserGroupRequestDTO(TypedDict):
    pass

class OptionalPermissionsToUserGroupRequestDTO(TypedDict, total=False):
    # The unique identifier associated with the user group.
    userGroupId: str

    permissionsIds: PermissionsToUserGroupRequestDTOPermissionsIds

class PermissionsToUserGroupRequestDTO(RequiredPermissionsToUserGroupRequestDTO, OptionalPermissionsToUserGroupRequestDTO):
    pass
