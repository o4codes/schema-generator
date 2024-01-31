import unittest
import tempfile

from schema_generator import SchemaGenerator
from . import utils


class TestInvalidData(unittest.TestCase):
    
    def test_input_file_not_found(self):
        input_file = "invalid_file.json"
        output_file = tempfile.NamedTemporaryFile(mode="r", suffix=".json")
        generator = SchemaGenerator(input_file, output_file.name)
        with self.assertRaises(Exception) as exc:
            generator.generate()
        self.assertEqual("Input File not found", str(exc.exception))
    
    
    def test_invalid_json_data(self):
        input_file = utils.write_json_to_temp_file("invalid_data")
        output_file = tempfile.NamedTemporaryFile(mode="r", suffix=".json")
        generator = SchemaGenerator(input_file.name, output_file.name)
        with self.assertRaises(Exception) as exc:
            generator.generate()
        self.assertEqual("Input data must be a dictionary", str(exc.exception))
    
    
    def test_invalid_data_structure(self):
        input_file = utils.write_json_to_temp_file({"attribute": "invalid_data"})
        output_file = tempfile.NamedTemporaryFile(mode="r", suffix=".json")
        generator = SchemaGenerator(input_file.name, output_file.name)
        with self.assertRaises(Exception) as exc:
            generator.generate()
        self.assertEqual("Input data must contain a 'message' key", str(exc.exception))