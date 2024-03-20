# coding: utf-8

"""
    Visier User Management APIs

    Visier APIs for managing users within an organization

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from visier_user_management_python_sdk import schemas  # noqa: F401


class UserGetAPIResponseDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            userId = schemas.StrSchema
            username = schemas.StrSchema
            displayName = schemas.StrSchema
            employeeId = schemas.StrSchema
            accountEnabled = schemas.BoolSchema
        
            @staticmethod
            def profiles() -> typing.Type['AllProfileAssignedForLocalTenantDTO']:
                return AllProfileAssignedForLocalTenantDTO
        
            @staticmethod
            def permissions() -> typing.Type['AllPermissionsAssignedForLocalTenantDTO']:
                return AllPermissionsAssignedForLocalTenantDTO
        
            @staticmethod
            def userGroups() -> typing.Type['AllUserGroupsAssignedForLocalTenantDTO']:
                return AllUserGroupsAssignedForLocalTenantDTO
        
            @staticmethod
            def lastLogin() -> typing.Type['LastLoginDTO']:
                return LastLoginDTO
            email = schemas.StrSchema
            __annotations__ = {
                "userId": userId,
                "username": username,
                "displayName": displayName,
                "employeeId": employeeId,
                "accountEnabled": accountEnabled,
                "profiles": profiles,
                "permissions": permissions,
                "userGroups": userGroups,
                "lastLogin": lastLogin,
                "email": email,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountEnabled"]) -> MetaOapg.properties.accountEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profiles"]) -> 'AllProfileAssignedForLocalTenantDTO': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> 'AllPermissionsAssignedForLocalTenantDTO': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userGroups"]) -> 'AllUserGroupsAssignedForLocalTenantDTO': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastLogin"]) -> 'LastLoginDTO': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["userId", "username", "displayName", "employeeId", "accountEnabled", "profiles", "permissions", "userGroups", "lastLogin", "email", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> typing.Union[MetaOapg.properties.employeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountEnabled"]) -> typing.Union[MetaOapg.properties.accountEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profiles"]) -> typing.Union['AllProfileAssignedForLocalTenantDTO', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> typing.Union['AllPermissionsAssignedForLocalTenantDTO', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userGroups"]) -> typing.Union['AllUserGroupsAssignedForLocalTenantDTO', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastLogin"]) -> typing.Union['LastLoginDTO', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["userId", "username", "displayName", "employeeId", "accountEnabled", "profiles", "permissions", "userGroups", "lastLogin", "email", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        userId: typing.Union[MetaOapg.properties.userId, str, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, schemas.Unset] = schemas.unset,
        accountEnabled: typing.Union[MetaOapg.properties.accountEnabled, bool, schemas.Unset] = schemas.unset,
        profiles: typing.Union['AllProfileAssignedForLocalTenantDTO', schemas.Unset] = schemas.unset,
        permissions: typing.Union['AllPermissionsAssignedForLocalTenantDTO', schemas.Unset] = schemas.unset,
        userGroups: typing.Union['AllUserGroupsAssignedForLocalTenantDTO', schemas.Unset] = schemas.unset,
        lastLogin: typing.Union['LastLoginDTO', schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserGetAPIResponseDTO':
        return super().__new__(
            cls,
            *args,
            userId=userId,
            username=username,
            displayName=displayName,
            employeeId=employeeId,
            accountEnabled=accountEnabled,
            profiles=profiles,
            permissions=permissions,
            userGroups=userGroups,
            lastLogin=lastLogin,
            email=email,
            _configuration=_configuration,
            **kwargs,
        )

from visier_user_management_python_sdk.model.all_permissions_assigned_for_local_tenant_dto import AllPermissionsAssignedForLocalTenantDTO
from visier_user_management_python_sdk.model.all_profile_assigned_for_local_tenant_dto import AllProfileAssignedForLocalTenantDTO
from visier_user_management_python_sdk.model.all_user_groups_assigned_for_local_tenant_dto import AllUserGroupsAssignedForLocalTenantDTO
from visier_user_management_python_sdk.model.last_login_dto import LastLoginDTO
