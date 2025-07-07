from enum import Enum


class RoleEnum(str,Enum):
    USER = "user"
    ADMIN = "admin"
    SUPER_ADMIN = "super_admin"