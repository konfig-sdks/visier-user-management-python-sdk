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


class RequiredUsersAPIErrorMessageDTO(TypedDict):
    pass

class OptionalUsersAPIErrorMessageDTO(TypedDict, total=False):
    # Error message
    message: str

    # The unique identifier associated to this error
    rci: str

class UsersAPIErrorMessageDTO(RequiredUsersAPIErrorMessageDTO, OptionalUsersAPIErrorMessageDTO):
    pass
