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


class LastLoginDTO(BaseModel):
    # The time that the user last logged into Visier.
    timestamp: typing.Optional[str] = Field(None, alias='timestamp')
    class Config:
        arbitrary_types_allowed = True
