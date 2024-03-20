import typing_extensions

from visier_user_management_python_sdk.paths import PathValues
from visier_user_management_python_sdk.apis.paths.v1_admin_permissions_users import V1AdminPermissionsUsers
from visier_user_management_python_sdk.apis.paths.v1_admin_permissions_permission_id_users import V1AdminPermissionsPermissionIdUsers
from visier_user_management_python_sdk.apis.paths.v1_admin_user_groups import V1AdminUserGroups
from visier_user_management_python_sdk.apis.paths.v1_admin_user_groups_permissions import V1AdminUserGroupsPermissions
from visier_user_management_python_sdk.apis.paths.v1_admin_user_groups_users import V1AdminUserGroupsUsers
from visier_user_management_python_sdk.apis.paths.v1_admin_user_groups_user_group_id_users import V1AdminUserGroupsUserGroupIdUsers
from visier_user_management_python_sdk.apis.paths.v1_admin_users import V1AdminUsers
from visier_user_management_python_sdk.apis.paths.v1_admin_users_user_id import V1AdminUsersUserId
from visier_user_management_python_sdk.apis.paths.v2_admin_users import V2AdminUsers
from visier_user_management_python_sdk.apis.paths.v1_admin_users_reports_application_logs import V1AdminUsersReportsApplicationLogs
from visier_user_management_python_sdk.apis.paths.v1_admin_users_user_id_reports_data_security import V1AdminUsersUserIdReportsDataSecurity
from visier_user_management_python_sdk.apis.paths.v1_admin_users_reports_profile_assignments import V1AdminUsersReportsProfileAssignments
from visier_user_management_python_sdk.apis.paths.v1_admin_users_reports_permission_assignments import V1AdminUsersReportsPermissionAssignments
from visier_user_management_python_sdk.apis.paths.v1_admin_users_reports_permissions_list import V1AdminUsersReportsPermissionsList

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_ADMIN_PERMISSIONS_USERS: V1AdminPermissionsUsers,
        PathValues.V1_ADMIN_PERMISSIONS_PERMISSION_ID_USERS: V1AdminPermissionsPermissionIdUsers,
        PathValues.V1_ADMIN_USERGROUPS: V1AdminUserGroups,
        PathValues.V1_ADMIN_USERGROUPS_PERMISSIONS: V1AdminUserGroupsPermissions,
        PathValues.V1_ADMIN_USERGROUPS_USERS: V1AdminUserGroupsUsers,
        PathValues.V1_ADMIN_USERGROUPS_USER_GROUP_ID_USERS: V1AdminUserGroupsUserGroupIdUsers,
        PathValues.V1_ADMIN_USERS: V1AdminUsers,
        PathValues.V1_ADMIN_USERS_USER_ID: V1AdminUsersUserId,
        PathValues.V2_ADMIN_USERS: V2AdminUsers,
        PathValues.V1_ADMIN_USERS_REPORTS_APPLICATIONLOGS: V1AdminUsersReportsApplicationLogs,
        PathValues.V1_ADMIN_USERS_USER_ID_REPORTS_DATASECURITY: V1AdminUsersUserIdReportsDataSecurity,
        PathValues.V1_ADMIN_USERS_REPORTS_PROFILEASSIGNMENTS: V1AdminUsersReportsProfileAssignments,
        PathValues.V1_ADMIN_USERS_REPORTS_PERMISSIONASSIGNMENTS: V1AdminUsersReportsPermissionAssignments,
        PathValues.V1_ADMIN_USERS_REPORTS_PERMISSIONSLIST: V1AdminUsersReportsPermissionsList,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_ADMIN_PERMISSIONS_USERS: V1AdminPermissionsUsers,
        PathValues.V1_ADMIN_PERMISSIONS_PERMISSION_ID_USERS: V1AdminPermissionsPermissionIdUsers,
        PathValues.V1_ADMIN_USERGROUPS: V1AdminUserGroups,
        PathValues.V1_ADMIN_USERGROUPS_PERMISSIONS: V1AdminUserGroupsPermissions,
        PathValues.V1_ADMIN_USERGROUPS_USERS: V1AdminUserGroupsUsers,
        PathValues.V1_ADMIN_USERGROUPS_USER_GROUP_ID_USERS: V1AdminUserGroupsUserGroupIdUsers,
        PathValues.V1_ADMIN_USERS: V1AdminUsers,
        PathValues.V1_ADMIN_USERS_USER_ID: V1AdminUsersUserId,
        PathValues.V2_ADMIN_USERS: V2AdminUsers,
        PathValues.V1_ADMIN_USERS_REPORTS_APPLICATIONLOGS: V1AdminUsersReportsApplicationLogs,
        PathValues.V1_ADMIN_USERS_USER_ID_REPORTS_DATASECURITY: V1AdminUsersUserIdReportsDataSecurity,
        PathValues.V1_ADMIN_USERS_REPORTS_PROFILEASSIGNMENTS: V1AdminUsersReportsProfileAssignments,
        PathValues.V1_ADMIN_USERS_REPORTS_PERMISSIONASSIGNMENTS: V1AdminUsersReportsPermissionAssignments,
        PathValues.V1_ADMIN_USERS_REPORTS_PERMISSIONSLIST: V1AdminUsersReportsPermissionsList,
    }
)
