[
    {
        "model": "tm_role.role",
        "pk": 1,
        "fields": {
            "name": "Administrator",
            "description": "Has full access to all features and settings.",
            "permissions": ["manage_users", "manage_content", "view_reports"]   // Change by TMPermissions
        }
    },
    {
        "model": "tm_role.role",
        "pk": 2,
        "fields": {
            "name": "Editor",
            "description": "Can edit and manage content but cannot change settings.",
            "permissions": ["edit_content", "view_reports"]
        }
    },
    {
        "model": "tm_role.role",
        "pk": 3,
        "fields": {
            "name": "Viewer",
            "description": "Can view content but cannot make any changes.",
            "permissions": ["view_content"]
        }
    }
]