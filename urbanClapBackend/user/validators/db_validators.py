from ..constants.enums import UserType


class DBValidators:

    @staticmethod
    def validate_user_type(user_type):
        if user_type in [e.value for e in UserType]:
            return True
        return False
