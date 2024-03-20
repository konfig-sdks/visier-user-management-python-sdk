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


class TenantAssignmentsDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            tenantCode = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def UNKNOWN(cls):
                    return cls("Unknown")
                
                @schemas.classproperty
                def SUCCEED(cls):
                    return cls("Succeed")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("Failed")
            message = schemas.StrSchema
            
            
            class assignments(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['UserSecurityAssignmentsDTO']:
                        return UserSecurityAssignmentsDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['UserSecurityAssignmentsDTO'], typing.List['UserSecurityAssignmentsDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'assignments':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UserSecurityAssignmentsDTO':
                    return super().__getitem__(i)
            __annotations__ = {
                "tenantCode": tenantCode,
                "status": status,
                "message": message,
                "assignments": assignments,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantCode"]) -> MetaOapg.properties.tenantCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignments"]) -> MetaOapg.properties.assignments: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tenantCode", "status", "message", "assignments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantCode"]) -> typing.Union[MetaOapg.properties.tenantCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignments"]) -> typing.Union[MetaOapg.properties.assignments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tenantCode", "status", "message", "assignments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tenantCode: typing.Union[MetaOapg.properties.tenantCode, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        assignments: typing.Union[MetaOapg.properties.assignments, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TenantAssignmentsDTO':
        return super().__new__(
            cls,
            *args,
            tenantCode=tenantCode,
            status=status,
            message=message,
            assignments=assignments,
            _configuration=_configuration,
            **kwargs,
        )

from visier_user_management_python_sdk.model.user_security_assignments_dto import UserSecurityAssignmentsDTO
