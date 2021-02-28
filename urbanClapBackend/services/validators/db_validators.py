from ..constants.enums import Status


class DBValidators:

    @staticmethod
    def validate_status(status):
        if status in [e.value for e in Status]:
            return True
        return False
