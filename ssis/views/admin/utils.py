from ssis.models.admin import Admin

def admin_found(username: str, password: str) -> bool:
    if Admin.validate(username, password):
        return True
    return False

