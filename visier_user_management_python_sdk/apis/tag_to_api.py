import typing_extensions

from visier_user_management_python_sdk.apis.tags import TagValues
from visier_user_management_python_sdk.apis.tags.user_management_api import UserManagementApi
from visier_user_management_python_sdk.apis.tags.user_management_v2_api import UserManagementV2Api

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.USER_MANAGEMENT: UserManagementApi,
        TagValues.USER_MANAGEMENT_V2: UserManagementV2Api,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.USER_MANAGEMENT: UserManagementApi,
        TagValues.USER_MANAGEMENT_V2: UserManagementV2Api,
    }
)
