from utils import EnvVars, ErrorMessages
from adaptors import DBAdaptor

if not EnvVars.POSTGRESQL_CONNECTION_STRING:
    raise ValueError(ErrorMessages.MISSING_DATA(["POSTGRESQL_CONNECTION_STRING"]))

db = DBAdaptor(EnvVars.POSTGRESQL_CONNECTION_STRING)