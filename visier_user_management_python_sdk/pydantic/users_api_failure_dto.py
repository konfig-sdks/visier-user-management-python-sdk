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

from visier_user_management_python_sdk.pydantic.users_api_error_message_dto import UsersAPIErrorMessageDTO

class UsersAPIFailureDTO(BaseModel):
    # The unique identifier associated with the user.
    user_id: typing.Optional[str] = Field(None, alias='userId')

    # The user's username. This is typically the user's email, such as john@jupiter.com.
    user_name: typing.Optional[str] = Field(None, alias='userName')

    # An identifiable name to display within Visier. For example, \"John Smith\".
    display_name: typing.Optional[str] = Field(None, alias='displayName')

    # The error thrown during creation.
    error: typing.Optional[UsersAPIErrorMessageDTO] = Field(None, alias='error')
    class Config:
        arbitrary_types_allowed = True
