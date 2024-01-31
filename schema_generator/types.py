from enum import Enum


class SchemaDataType(Enum):
    STRING = "STRING"
    INTEGER = "INTEGER"
    ENUM = "ENUM"
    ARRAY = "ARRAY"
    OBJECT = "OBJECT"
    BOOLEAN = "BOOLEAN"

TYPE_MAPPING = {
    str: SchemaDataType.STRING,
    int: SchemaDataType.INTEGER,
    list: {
        str: SchemaDataType.ENUM,
        dict: SchemaDataType.ARRAY
    },
    dict: SchemaDataType.OBJECT,
    bool: SchemaDataType.BOOLEAN
}
