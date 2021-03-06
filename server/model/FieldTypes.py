from enum import Enum

# FieldTypes : Stores the various MySQL field types
class FieldTypes(Enum):
    VARCHAR = 1,
    TEXT = 2,
    INTEGER = 3,
    INT = 4,
    BIGINT = 5,
    FLOAT = 6,
    DOUBLE = 7,
    DATE = 8,
    TIMESTAMP = 9,
