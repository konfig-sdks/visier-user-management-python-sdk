from visier_user_management_python_sdk.paths.v2_admin_users.put import ApiForput
from visier_user_management_python_sdk.paths.v2_admin_users.post import ApiForpost
from visier_user_management_python_sdk.paths.v2_admin_users.delete import ApiFordelete


class V2AdminUsers(
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
