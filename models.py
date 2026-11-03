from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, id, username, role, campus_id=None, full_name="Unknown"):
        # ENCAPSULATION: We use an underscore (_) to mark these as "protected" attributes.
        # They should only be accessed through the @property getters below.
        self._user_id = id
        self._username = username
        self._role = role
        self._campus_id = campus_id
        self._full_name = full_name

    # Getters (Properties) allow read-only access to the encapsulated data
    @property
    def user_id(self):
        return self._user_id

    @property
    def username(self):
        return self._username

    @property
    def role(self):
        return self._role

    @property
    def campus_id(self):
        return self._campus_id

    @property
    def full_name(self):
        return self._full_name

    @abstractmethod
    def dashboard_permissions(self):
        """Each specific role must define what they are allowed to do."""
        pass


class Lecturer(User):
    def dashboard_permissions(self):
        return ["view_resources", "create_booking", "view_own_bookings", "cancel_booking"]


class CampusAdmin(User):
    def dashboard_permissions(self):
        return ["add_resource", "update_resource", "remove_resource", "view_campus_bookings", "monitor_usage"]


class SystemOperator(User):
    def dashboard_permissions(self):
        return ["view_all_bookings", "view_all_resources", "generate_cross_campus_report"]


def create_user_object(user_dict):
    """Factory function to convert a database dictionary into a Python Object."""
    if not user_dict:
        return None

    role = user_dict.get("role")
    # We map the dictionary keys to the expected __init__ arguments
    kwargs = {
        "id": user_dict.get("id"),
        "username": user_dict.get("username"),
        "role": role,
        "campus_id": user_dict.get("campus_id"),
        "full_name": user_dict.get("full_name"),
    }

    if role == "lecturer":
        return Lecturer(**kwargs)
    elif role == "admin":
        return CampusAdmin(**kwargs)
    elif role == "operator":
        return SystemOperator(**kwargs)

    # Fallback (though User is abstract, this handles unexpected roles)
    raise ValueError(f"Unknown role: {role}")