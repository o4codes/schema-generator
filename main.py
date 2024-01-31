"""
Main file to utilize the schema generator
"""

from executors.schema_generator import SchemaGenerator

input_file_one = "data/data_1.json"
input_file_two = "data/data_2.json"
output_file_one = "schema/schema_1.json"
output_file_two = "schema/schema_2.json"

schema_generator = SchemaGenerator(input_file_one, output_file_one)
schema_generator.generate()

schema_generator = SchemaGenerator(input_file_two, output_file_two)
schema_generator.generate()
