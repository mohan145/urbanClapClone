from ..constants.enums import Type


class DBValidators:

    @staticmethod
    def validate_type(type):
        if type in [e.value for e in Type]:
            return True
        return False
