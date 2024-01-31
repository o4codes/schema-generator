import json
import unittest
import tempfile

from schema_generator import SchemaGenerator
from . import utils


class TestValidData(unittest.TestCase):
    def test_simple_data(self):
        input_data = {"message": {"name": "name", "count": 2}}
        expected_result = {
            "name": {"type": "string", "tag": "", "description": "", "required": False},
            "count": {
                "type": "integer",
                "tag": "",
                "description": "",
                "required": False,
            },
        }
        input_file = utils.write_json_to_temp_file(input_data)
        output_file = tempfile.NamedTemporaryFile(mode="r", suffix=".json")
        generator = SchemaGenerator(input_file.name, output_file.name)
        generator.generate()
        output_data = json.load(output_file)
        self.assertDictEqual(expected_result, output_data)

    def test_array_object_data(self):
        input_data = {"message": {"items": [{"name": "name", "count": 2}]}}
        expected_result = {
            "items": {
                "type": "array",
                "tag": "",
                "description": "",
                "required": False,
                "attrs": [
                    {
                        "name": {
                            "type": "string",
                            "tag": "",
                            "description": "",
                            "required": False,
                        },
                        "count": {
                            "type": "integer",
                            "tag": "",
                            "description": "",
                            "required": False,
                        },
                    }
                ],
            }
        }
        input_file = utils.write_json_to_temp_file(input_data)
        output_file = tempfile.NamedTemporaryFile(mode="r", suffix=".json")
        generator = SchemaGenerator(input_file.name, output_file.name)
        generator.generate()
        output_data = json.load(output_file)
        self.assertDictEqual(expected_result, output_data)

    def test_object_data(self):
        input_data = {"message": {"items": {"name": "name", "count": 2}}}
        expected_result = {
            "items": {
                "type": "object",
                "tag": "",
                "description": "",
                "required": False,
                "attrs": {
                    "name": {
                        "type": "string",
                        "tag": "",
                        "description": "",
                        "required": False,
                    },
                    "count": {
                        "type": "integer",
                        "tag": "",
                        "description": "",
                        "required": False,
                    },
                },
            }
        }

        input_file = utils.write_json_to_temp_file(input_data)
        output_file = tempfile.NamedTemporaryFile(mode="r", suffix=".json")
        generator = SchemaGenerator(input_file.name, output_file.name)
        generator.generate()
        output_data = json.load(output_file)
        self.assertDictEqual(expected_result, output_data)
