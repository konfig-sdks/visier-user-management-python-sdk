<div align="center">

[![Visit Visier](./header.png)](https://visier.com)

# Visier<a id="visier"></a>

Visier APIs for managing users within an organization


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`visierusermanagement.user_management.add_user`](#visierusermanagementuser_managementadd_user)
  * [`visierusermanagement.user_management.add_users_to_user_group`](#visierusermanagementuser_managementadd_users_to_user_group)
  * [`visierusermanagement.user_management.assign_permissions`](#visierusermanagementuser_managementassign_permissions)
  * [`visierusermanagement.user_management.assign_permissions_to_user_groups`](#visierusermanagementuser_managementassign_permissions_to_user_groups)
  * [`visierusermanagement.user_management.delete_user`](#visierusermanagementuser_managementdelete_user)
  * [`visierusermanagement.user_management.get_all_permissions_xlsx`](#visierusermanagementuser_managementget_all_permissions_xlsx)
  * [`visierusermanagement.user_management.get_all_user_groups`](#visierusermanagementuser_managementget_all_user_groups)
  * [`visierusermanagement.user_management.get_all_users`](#visierusermanagementuser_managementget_all_users)
  * [`visierusermanagement.user_management.get_application_logs_xlsx`](#visierusermanagementuser_managementget_application_logs_xlsx)
  * [`visierusermanagement.user_management.get_data_security_report_xlsx`](#visierusermanagementuser_managementget_data_security_report_xlsx)
  * [`visierusermanagement.user_management.get_permission_assigned_users`](#visierusermanagementuser_managementget_permission_assigned_users)
  * [`visierusermanagement.user_management.get_profile_assignments_xlsx`](#visierusermanagementuser_managementget_profile_assignments_xlsx)
  * [`visierusermanagement.user_management.get_user_detail`](#visierusermanagementuser_managementget_user_detail)
  * [`visierusermanagement.user_management.get_user_group_users`](#visierusermanagementuser_managementget_user_group_users)
  * [`visierusermanagement.user_management.get_user_permissions_xlsx`](#visierusermanagementuser_managementget_user_permissions_xlsx)
  * [`visierusermanagement.user_management.remove_permissions`](#visierusermanagementuser_managementremove_permissions)
  * [`visierusermanagement.user_management.remove_users_from_user_group`](#visierusermanagementuser_managementremove_users_from_user_group)
  * [`visierusermanagement.user_management.revoke_permissions_from_user_groups`](#visierusermanagementuser_managementrevoke_permissions_from_user_groups)
  * [`visierusermanagement.user_management.update_user`](#visierusermanagementuser_managementupdate_user)
  * [`visierusermanagement.user_management_v2.add_users`](#visierusermanagementuser_management_v2add_users)
  * [`visierusermanagement.user_management_v2.delete_users`](#visierusermanagementuser_management_v2delete_users)
  * [`visierusermanagement.user_management_v2.update_users`](#visierusermanagementuser_management_v2update_users)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Visier&serviceName=UserManagement&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from visier_user_management_python_sdk import VisierUserManagement, ApiException

visierusermanagement = VisierUserManagement(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Add a user
    add_user_response = visierusermanagement.user_management.add_user(
        username="string_example",
        display_name="string_example",
        employee_id="string_example",
        account_enabled="string_example",
        email="string_example",
        tenant_code="string_example",
    )
    print(add_user_response)
except ApiException as e:
    print("Exception when calling UserManagementApi.add_user: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from visier_user_management_python_sdk import VisierUserManagement, ApiException

visierusermanagement = VisierUserManagement(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Add a user
        add_user_response = await visierusermanagement.user_management.aadd_user(
            username="string_example",
            display_name="string_example",
            employee_id="string_example",
            account_enabled="string_example",
            email="string_example",
            tenant_code="string_example",
        )
        print(add_user_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi.add_user: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from visier_user_management_python_sdk import VisierUserManagement, ApiException

visierusermanagement = VisierUserManagement(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Add a user
    add_user_response = visierusermanagement.user_management.raw.add_user(
        username="string_example",
        display_name="string_example",
        employee_id="string_example",
        account_enabled="string_example",
        email="string_example",
        tenant_code="string_example",
    )
    pprint(add_user_response.body)
    pprint(add_user_response.body["user_id"])
    pprint(add_user_response.body["username"])
    pprint(add_user_response.body["display_name"])
    pprint(add_user_response.body["employee_id"])
    pprint(add_user_response.body["account_enabled"])
    pprint(add_user_response.body["email"])
    pprint(add_user_response.headers)
    pprint(add_user_response.status)
    pprint(add_user_response.round_trip_time)
except ApiException as e:
    print("Exception when calling UserManagementApi.add_user: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `visierusermanagement.user_management.add_user`<a id="visierusermanagementuser_managementadd_user"></a>

This API allows you to create a new user. Administrating tenant users can specify the tenant in which to add a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_user_response = visierusermanagement.user_management.add_user(
    username="string_example",
    display_name="string_example",
    employee_id="string_example",
    account_enabled="string_example",
    email="string_example",
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

The user's username. This is typically the user's email, such as john@visier.com.

##### display_name: `str`<a id="display_name-str"></a>

An identifiable name to display within Visier. For example, \\\"John Smith\\\".

##### employee_id: `str`<a id="employee_id-str"></a>

If applicable, and if available, the user employee ID in the data.

##### account_enabled: `str`<a id="account_enabled-str"></a>

If false, the user account is disabled.

##### email: `str`<a id="email-str"></a>

The user's email. This is used if the user's email is different from their username. For example, \\\"john.doe@visier.com\\\".

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to create a user in.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserCreationAPIRequestDTO`](./visier_user_management_python_sdk/type/user_creation_api_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserCreationAPIResponseDTO`](./visier_user_management_python_sdk/pydantic/user_creation_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.add_users_to_user_group`<a id="visierusermanagementuser_managementadd_users_to_user_group"></a>

This API allows you to assign users to specific user groups.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_users_to_user_group_response = visierusermanagement.user_management.add_users_to_user_group(
    user_groups=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_groups: List[`UsersToUserGroupRequestDTO`]<a id="user_groups-listuserstousergrouprequestdto"></a>

A list of objects representing the user groups and users to assign or remove.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersToUserGroupsRequestDTO`](./visier_user_management_python_sdk/type/users_to_user_groups_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SecurityAssignmentResponseDTO`](./visier_user_management_python_sdk/pydantic/security_assignment_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/user-groups/users` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.assign_permissions`<a id="visierusermanagementuser_managementassign_permissions"></a>

This API allows you to assign a permission to specific users. Administrating tenant users can assign permissions
 to users in the administrating tenant and in the analytic tenants those users belong to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_permissions_response = visierusermanagement.user_management.assign_permissions(
    permissions=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### permissions: List[`Permission`]<a id="permissions-listpermission"></a>

A list of objects representing the permissions to assign to or remove from users.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AssignRevokePermissionsRequest`](./visier_user_management_python_sdk/type/assign_revoke_permissions_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AssignRevokePermissionsResponseDTO`](./visier_user_management_python_sdk/pydantic/assign_revoke_permissions_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/permissions/users` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.assign_permissions_to_user_groups`<a id="visierusermanagementuser_managementassign_permissions_to_user_groups"></a>

This API allows you to assign a permission to specific user groups. This assigns the permission to all users in the user group.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_permissions_to_user_groups_response = visierusermanagement.user_management.assign_permissions_to_user_groups(
    user_groups=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_groups: List[`PermissionsToUserGroupRequestDTO`]<a id="user_groups-listpermissionstousergrouprequestdto"></a>

A list of objects representing the user groups and permissions to assign or remove.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PermissionsToUserGroupsRequestDTO`](./visier_user_management_python_sdk/type/permissions_to_user_groups_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PermissionsToUserGroupForTenantDTO`](./visier_user_management_python_sdk/pydantic/permissions_to_user_group_for_tenant_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/user-groups/permissions` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.delete_user`<a id="visierusermanagementuser_managementdelete_user"></a>

This API allows you to delete an existing user. Administrating tenant users can specify the tenant from which to delete a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_user_response = visierusermanagement.user_management.delete_user(
    user_id="userId_example",
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user you want to delete.

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to delete a user in.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/users/{userId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.get_all_permissions_xlsx`<a id="visierusermanagementuser_managementget_all_permissions_xlsx"></a>

This API allows you to export the list of permissions in a tenant. This report includes the permission name,
 permission description, and permission ID for all permissions in the tenant.

 Administrating tenant users can export permissions lists for the administrating tenant and the analytic tenants
 those users belong to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_permissions_xlsx_response = visierusermanagement.user_management.get_all_permissions_xlsx(
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to retrieve permissions from.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/users/reports/permissions-list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.get_all_user_groups`<a id="visierusermanagementuser_managementget_all_user_groups"></a>

This API allows you to retrieve the full list of user groups in a tenant.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_user_groups_response = visierusermanagement.user_management.get_all_user_groups(
    tenant_code="string_example",
    limit=1,
    start=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to retrieve the list of user groups from.

##### limit: `int`<a id="limit-int"></a>

The number of results to return. The maximum number of users to retrieve is 1000.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset.

#### 🔄 Return<a id="🔄-return"></a>

[`UserGroupsGetAPIResponseDTO`](./visier_user_management_python_sdk/pydantic/user_groups_get_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/user-groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.get_all_users`<a id="visierusermanagementuser_managementget_all_users"></a>

This API allows you to retrieve the full list of users and their current states.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_users_response = visierusermanagement.user_management.get_all_users(
    tenant_code="string_example",
    assigned_profiles=True,
    assigned_permissions=True,
    assigned_user_groups=True,
    limit=1,
    start=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to retrieve a list of users from.

##### assigned_profiles: `bool`<a id="assigned_profiles-bool"></a>

If true, the response returns a list of the user's assigned profiles.

##### assigned_permissions: `bool`<a id="assigned_permissions-bool"></a>

If true, the response returns the user's assigned permissions.

##### assigned_user_groups: `bool`<a id="assigned_user_groups-bool"></a>

If true, the response returns the user's assigned user groups.

##### limit: `int`<a id="limit-int"></a>

The number of results to return. The maximum number of users to retrieve is 1000.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

#### 🔄 Return<a id="🔄-return"></a>

[`AllUsersGetAPIResponseDTO`](./visier_user_management_python_sdk/pydantic/all_users_get_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.get_application_logs_xlsx`<a id="visierusermanagementuser_managementget_application_logs_xlsx"></a>

This API allows you to export the Application Logs for a tenant. The Application Logs track information about your
 users and how they are using the application. Performing regular audits will help you identify potential security
 issues and keep your data safe. As part of user management, download the Application Logs to monitor user activity
 and logon events to ensure your users are performing authorized activities.

 Administrating tenant users can export application logs for the administrating tenant and the analytic tenants
 those users belong to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_application_logs_xlsx_response = visierusermanagement.user_management.get_application_logs_xlsx(
    start_time="string_example",
    end_time="string_example",
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_time: `str`<a id="start_time-str"></a>

An inclusive date-time to start retrieving Application Logs from.

##### end_time: `str`<a id="end_time-str"></a>

An exclusive date-time to stop retrieving Application Logs from.

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to retrieve Application Logs from.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/users/reports/application-logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.get_data_security_report_xlsx`<a id="visierusermanagementuser_managementget_data_security_report_xlsx"></a>

This API allows you to export the data security report of a user. The Data Security Report provides information
 about a specific user to see which populations and properties that user has access to as a result of the
 permissions assigned to them.

 Administrating tenant users can export the report for users in the administrating tenant and the analytic
 tenants those users belong to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_data_security_report_xlsx_response = visierusermanagement.user_management.get_data_security_report_xlsx(
    user_id="userId_example",
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user to retrieve the report for.

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to retrieve the Data Security Report from.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/users/{userId}/reports/data-security` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.get_permission_assigned_users`<a id="visierusermanagementuser_managementget_permission_assigned_users"></a>

This API allows you to retrieve all the users that are assigned a specified permission. You must know the ID
 of the permission you want to retrieve users for.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_permission_assigned_users_response = visierusermanagement.user_management.get_permission_assigned_users(
    permission_id="permissionId_example",
    include_user_groups=True,
    tenant_filter="string_example",
    limit=1,
    start=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### permission_id: `str`<a id="permission_id-str"></a>

The unique identifier of the permission you want to retrieve users for.

##### include_user_groups: `bool`<a id="include_user_groups-bool"></a>

If true, the response returns a list of all users that are assigned the permission, including users that are  assigned the permission through a user group. If false, the response returns a list of the users that are directly assigned the permission.

##### tenant_filter: `str`<a id="tenant_filter-str"></a>

Specify the tenant to retrieve the list of users from.

##### limit: `int`<a id="limit-int"></a>

The number of results to return. The maximum number of tenants to retrieve is 100.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

#### 🔄 Return<a id="🔄-return"></a>

[`PermissionAssignedUsersDTO`](./visier_user_management_python_sdk/pydantic/permission_assigned_users_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/permissions/{permissionId}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.get_profile_assignments_xlsx`<a id="visierusermanagementuser_managementget_profile_assignments_xlsx"></a>

This API allows you to export the profiles assigned to each user. This report details the profiles assigned to
 each user and the profile validity period.

 Administrating tenant users can export profile assignments for the administrating tenant and the analytic tenants
 those users belong to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_profile_assignments_xlsx_response = visierusermanagement.user_management.get_profile_assignments_xlsx(
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to retrieve profile assignments from.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/users/reports/profile-assignments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.get_user_detail`<a id="visierusermanagementuser_managementget_user_detail"></a>

This API allows you to retrieve all details for a specified user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_detail_response = visierusermanagement.user_management.get_user_detail(
    user_id="userId_example",
    tenant_code="string_example",
    assigned_profiles=True,
    assigned_permissions=True,
    assigned_user_groups=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user you want to retrieve.

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to retrieve a user from.

##### assigned_profiles: `bool`<a id="assigned_profiles-bool"></a>

If true, the response returns a list of the user's assigned profiles.

##### assigned_permissions: `bool`<a id="assigned_permissions-bool"></a>

If true, the response returns the user's assigned permissions.

##### assigned_user_groups: `bool`<a id="assigned_user_groups-bool"></a>

If true, the response returns the user's assigned user groups.

#### 🔄 Return<a id="🔄-return"></a>

[`UserGetAPIResponseDTO`](./visier_user_management_python_sdk/pydantic/user_get_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/users/{userId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.get_user_group_users`<a id="visierusermanagementuser_managementget_user_group_users"></a>

This API allows you to retrieve the list of users explicitly assigned to a user group. Users that are implicitly
 included in the user group through the user group's dynamic filters are not returned by this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_group_users_response = visierusermanagement.user_management.get_user_group_users(
    user_group_id="userGroupId_example",
    tenant_filter="string_example",
    limit=1,
    start=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_group_id: `str`<a id="user_group_id-str"></a>

The ID of user group.

##### tenant_filter: `str`<a id="tenant_filter-str"></a>

Specifies the tenant to retrieve the list of users from.

##### limit: `int`<a id="limit-int"></a>

The number of results to return. The maximum number of tenants to retrieve is 100.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

#### 🔄 Return<a id="🔄-return"></a>

[`UserGroupsUsersDTO`](./visier_user_management_python_sdk/pydantic/user_groups_users_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/user-groups/{userGroupId}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.get_user_permissions_xlsx`<a id="visierusermanagementuser_managementget_user_permissions_xlsx"></a>

This API allows you to export the user permission assignments for a tenant. The permission assignments report
 provides a summary of the permissions your users have been assigned and how each permission is being used across
 your user base, as well as the users that do not have any permissions assigned to them.

 Administrating tenant users can export permission assignments for the administrating tenant and the analytic
 tenants those users belong to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_permissions_xlsx_response = visierusermanagement.user_management.get_user_permissions_xlsx(
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to retrieve the permission assignments report from.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/users/reports/permission-assignments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.remove_permissions`<a id="visierusermanagementuser_managementremove_permissions"></a>

This API allows you to remove a permission from specific users. Administrating tenant users can remove permissions
 from users in the administrating tenant and in the analytic tenants those users belong to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_permissions_response = visierusermanagement.user_management.remove_permissions(
    permissions=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### permissions: List[`Permission`]<a id="permissions-listpermission"></a>

A list of objects representing the permissions to assign to or remove from users.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AssignRevokePermissionsRequest`](./visier_user_management_python_sdk/type/assign_revoke_permissions_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AssignRevokePermissionsResponseDTO`](./visier_user_management_python_sdk/pydantic/assign_revoke_permissions_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/permissions/users` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.remove_users_from_user_group`<a id="visierusermanagementuser_managementremove_users_from_user_group"></a>

This API allows you to remove users from specific user groups.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_users_from_user_group_response = visierusermanagement.user_management.remove_users_from_user_group(
    user_groups=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_groups: List[`UsersToUserGroupRequestDTO`]<a id="user_groups-listuserstousergrouprequestdto"></a>

A list of objects representing the user groups and users to assign or remove.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersToUserGroupsRequestDTO`](./visier_user_management_python_sdk/type/users_to_user_groups_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SecurityAssignmentResponseDTO`](./visier_user_management_python_sdk/pydantic/security_assignment_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/user-groups/users` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.revoke_permissions_from_user_groups`<a id="visierusermanagementuser_managementrevoke_permissions_from_user_groups"></a>

This API allows you to remove a permission from specific user groups.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
revoke_permissions_from_user_groups_response = visierusermanagement.user_management.revoke_permissions_from_user_groups(
    user_groups=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_groups: List[`PermissionsToUserGroupRequestDTO`]<a id="user_groups-listpermissionstousergrouprequestdto"></a>

A list of objects representing the user groups and permissions to assign or remove.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PermissionsToUserGroupsRequestDTO`](./visier_user_management_python_sdk/type/permissions_to_user_groups_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PermissionsToUserGroupForTenantDTO`](./visier_user_management_python_sdk/pydantic/permissions_to_user_group_for_tenant_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/user-groups/permissions` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management.update_user`<a id="visierusermanagementuser_managementupdate_user"></a>

This API allows you to update an existing user's information, such as their display name or if the user is enabled in Visier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_user_response = visierusermanagement.user_management.update_user(
    user_id="userId_example",
    display_name="string_example",
    employee_id="string_example",
    account_enabled="string_example",
    email="string_example",
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user you want to update.

##### display_name: `str`<a id="display_name-str"></a>

An identifiable name to display within Visier. For example, \\\"John Smith\\\".

##### employee_id: `str`<a id="employee_id-str"></a>

If applicable, and if available, the user employee ID in the data.

##### account_enabled: `str`<a id="account_enabled-str"></a>

If true, the user account is enabled.

##### email: `str`<a id="email-str"></a>

The user's email address.

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to update a user in.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserUpdateAPIRequestDTO`](./visier_user_management_python_sdk/type/user_update_api_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserUpdateAPIRequestDTO`](./visier_user_management_python_sdk/pydantic/user_update_api_request_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/users/{userId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management_v2.add_users`<a id="visierusermanagementuser_management_v2add_users"></a>

This API allows you to create new users. Administrating tenant users can specify the tenant in which to add these users.

 <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_users_response = visierusermanagement.user_management_v2.add_users(
    users=[
        {
        }
    ],
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### users: List[`UserCreationAPIRequestDTO`]<a id="users-listusercreationapirequestdto"></a>

A list of objects representing users to create.

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to create a user in.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreationAPIRequestDTO`](./visier_user_management_python_sdk/type/users_creation_api_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersAPIResponseDTO`](./visier_user_management_python_sdk/pydantic/users_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/admin/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management_v2.delete_users`<a id="visierusermanagementuser_management_v2delete_users"></a>

This API allows you to delete an existing user. Administrating tenant users can specify the tenant from which to delete a user.

 <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_users_response = visierusermanagement.user_management_v2.delete_users(
    user_ids=[
        "string_example"
    ],
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_ids: [`UsersDeleteAPIRequestDTOUserIds`](./visier_user_management_python_sdk/type/users_delete_api_request_dto_user_ids.py)<a id="user_ids-usersdeleteapirequestdtouseridsvisier_user_management_python_sdktypeusers_delete_api_request_dto_user_idspy"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to delete a user in.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersDeleteAPIRequestDTO`](./visier_user_management_python_sdk/type/users_delete_api_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersAPIResponseDTO`](./visier_user_management_python_sdk/pydantic/users_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/admin/users` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierusermanagement.user_management_v2.update_users`<a id="visierusermanagementuser_management_v2update_users"></a>

This API allows you to update an existing user's information, such as their display name or if the user is enabled in Visier.

 <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_users_response = visierusermanagement.user_management_v2.update_users(
    users=[
        {
        }
    ],
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### users: List[`UsersUpdateAPIUserDTO`]<a id="users-listusersupdateapiuserdto"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

Specify the tenant to update a user in.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateAPIRequestDTO`](./visier_user_management_python_sdk/type/users_update_api_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersAPIResponseDTO`](./visier_user_management_python_sdk/pydantic/users_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/admin/users` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
