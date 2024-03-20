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


class RequiredAssignRevokePermissionByUserDTO(TypedDict):
    pass

class OptionalAssignRevokePermissionByUserDTO(TypedDict, total=False):
    # The unique identifier associated with the user.
    userId: str

    # The user's username. This is typically the user's email, such as john@visier.com.
    username: str

    # A meaningful message about the user permission.
    message: str

class AssignRevokePermissionByUserDTO(RequiredAssignRevokePermissionByUserDTO, OptionalAssignRevokePermissionByUserDTO):
    pass
