# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from visier_user_management_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    USER_MANAGEMENT = "UserManagement"
    USER_MANAGEMENT_V2 = "UserManagementV2"
