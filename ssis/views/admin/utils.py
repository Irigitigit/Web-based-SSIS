from ssis.models.admin import Admin

def admin_found(username: str, password: str) -> bool:
    return Admin.validate(username, password)

