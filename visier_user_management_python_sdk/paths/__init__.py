# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from visier_user_management_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_ADMIN_PERMISSIONS_USERS = "/v1/admin/permissions/users"
    V1_ADMIN_PERMISSIONS_PERMISSION_ID_USERS = "/v1/admin/permissions/{permissionId}/users"
    V1_ADMIN_USERGROUPS = "/v1/admin/user-groups"
    V1_ADMIN_USERGROUPS_PERMISSIONS = "/v1/admin/user-groups/permissions"
    V1_ADMIN_USERGROUPS_USERS = "/v1/admin/user-groups/users"
    V1_ADMIN_USERGROUPS_USER_GROUP_ID_USERS = "/v1/admin/user-groups/{userGroupId}/users"
    V1_ADMIN_USERS = "/v1/admin/users"
    V1_ADMIN_USERS_USER_ID = "/v1/admin/users/{userId}"
    V2_ADMIN_USERS = "/v2/admin/users"
    V1_ADMIN_USERS_REPORTS_APPLICATIONLOGS = "/v1/admin/users/reports/application-logs"
    V1_ADMIN_USERS_USER_ID_REPORTS_DATASECURITY = "/v1/admin/users/{userId}/reports/data-security"
    V1_ADMIN_USERS_REPORTS_PROFILEASSIGNMENTS = "/v1/admin/users/reports/profile-assignments"
    V1_ADMIN_USERS_REPORTS_PERMISSIONASSIGNMENTS = "/v1/admin/users/reports/permission-assignments"
    V1_ADMIN_USERS_REPORTS_PERMISSIONSLIST = "/v1/admin/users/reports/permissions-list"
