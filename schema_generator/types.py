from enum import Enum


class SchemaDataType(Enum):
    STRING = "string"
    INTEGER = "integer"
    ENUM = "enum"
    ARRAY = "array"
    OBJECT = "object"
    BOOLEAN = "boolean"

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
