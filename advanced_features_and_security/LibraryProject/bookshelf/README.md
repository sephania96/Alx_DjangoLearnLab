# Permissions and Groups Setup

This application uses Django's built-in permission system to control access to certain parts of the application.

## Groups

The following groups are set up:

* Editors: Can create, edit, and delete books
* Viewers: Can view books
* Admins: Can perform all actions

## Permissions

The following permissions are defined:

* can_view: Can view books
* can_create: Can create books
* can_edit: Can edit books
* can_delete: Can delete books

## Assigning Permissions to Groups

To assign permissions to groups, go to the Django admin site and navigate to the "Groups" section. Select the group you want to assign permissions to and click on the "Permissions" tab. Select the permissions you want to assign to the group and click "Save".

## Testing Permissions

To test permissions, create test users and assign them to different groups. Log in as these users and attempt to access various parts of the application to ensure that permissions are applied correctly.