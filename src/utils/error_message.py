class ErrorMessages:

    @staticmethod
    def MISSING_DATA(missing_fields, context=""):
        return f"Required data is missing: {', '.join(missing_fields)}. Please provide the missing fields to continue. {context}"