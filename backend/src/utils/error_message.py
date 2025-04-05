class ErrorMessages:

    @staticmethod
    def MISSING_DATA(missing_fields, context=""):
        return f"Required data is missing: {', '.join(missing_fields)}. Please provide the missing fields to continue. {context}"
    
    @staticmethod
    def EXCEPTION(context):
        return f"Error occured while {context}."
    
    @staticmethod
    def NOT_FOUND(context):
        return f"Not found: {context}"