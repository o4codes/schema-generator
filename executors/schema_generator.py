import json
from typing import Any, Optional, Union
from executors.schema_types import SchemaDataType, TYPE_MAPPING

class SchemaGenerator:
    """Generates a schema description of a json object
    """
    
    def __init__(self, input_file_path: str, output_file_path: str):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self._schema = {}
        self._input_data = None
    
    def generate(self):
        """
        Generates a schema description of the input data.
        Write schema description to output file
        """
        self._read_input_file()
        self._validate_input_data()
        self._generate_schema()
        self._write_schema_to_output_file()
    
    def _read_input_file(self) -> Union[list, dict]:
        """
        Reads input file and returns the json decoded data
        :raises Exception: if input file is not found
        :raises Exception: if input file content is not a valid JSON
        :return: Union[list, dict]: decoded content of input file
        """
        try:
            with open(self.input_file_path, "r") as f:
                self._input_data = json.load(f)
        except FileNotFoundError as exc:
            raise Exception("Input File not found") from exc
        except json.JSONDecodeError as exc:
            raise Exception("Input File is not valid JSON") from exc

    def _validate_input_data(self):
        """ 
        Validates Input data
        :raises Exception: if input data is empty
        :raises Exception: if input data is not a dictionary
        :raises Exception: if input data does not contain a 'message' key
        """
        if not self._input_data:
            raise Exception("Input data is empty")
        if not isinstance(self._input_data, dict):
            raise Exception("Input data must be a dictionary")
        if not self._input_data.get("message"):
            raise Exception("Input data must contain a 'message' key")

    def _generate_schema(self):
        """
        Parses the input data and generates a schema description
        """
        self._schema = self._parse_schema(self._input_data["message"])
    
    def _parse_schema(self, data: dict):
        schema = {}
        for key, value in data.items():
            data_type = self._infer_data_type(value)
            if not data_type:
                continue
            schema[key] = {
                "type": data_type.value,
                "tag": "",
                "description": "",
                "required": False,
            }
            if data_type == SchemaDataType.OBJECT:
                attrs = self._parse_schema(value)
                schema[key]["attrs"] = attrs
            if data_type == SchemaDataType.ARRAY:
                attrs = []
                for element in value:
                    attr = self._parse_schema(element)
                    attrs.append(attr)
                schema[key]["attrs"] = attrs
        return schema

    @classmethod
    def _infer_data_type(self, value: Any) -> Optional[SchemaDataType]:
        """
        Infers the schema data type of the value being passed
        :param value: Value being passed
        :return: SchemaDataType
        """
        value_type = type(value)
        if value_type is list:
            if not value:
                return SchemaDataType.ENUM
            element_type = type(value[0])
            return TYPE_MAPPING.get(value_type, {}).get(element_type)
        return TYPE_MAPPING.get(value_type)
    
    def _write_schema_to_output_file(self):
        """
        Writes generated schema to output file
        :raise: Exception: if schema is empty
        """
        if not self._schema:
            raise Exception("Schema is empty and has not been generated")
        with open(self.output_file_path, "w") as f:
            json.dump(self._schema, f)