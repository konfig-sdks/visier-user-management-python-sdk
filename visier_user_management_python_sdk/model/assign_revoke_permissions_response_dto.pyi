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


class AssignRevokePermissionsResponseDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The results of the permission assignment or removal.
    """


    class MetaOapg:
        
        class properties:
            
            
            class tenants(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AssignRevokePermissionByTenantDTO']:
                        return AssignRevokePermissionByTenantDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AssignRevokePermissionByTenantDTO'], typing.List['AssignRevokePermissionByTenantDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tenants':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AssignRevokePermissionByTenantDTO':
                    return super().__getitem__(i)
            __annotations__ = {
                "tenants": tenants,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenants"]) -> MetaOapg.properties.tenants: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tenants", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenants"]) -> typing.Union[MetaOapg.properties.tenants, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tenants", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tenants: typing.Union[MetaOapg.properties.tenants, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AssignRevokePermissionsResponseDTO':
        return super().__new__(
            cls,
            *args,
            tenants=tenants,
            _configuration=_configuration,
            **kwargs,
        )

from visier_user_management_python_sdk.model.assign_revoke_permission_by_tenant_dto import AssignRevokePermissionByTenantDTO
