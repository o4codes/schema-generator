# Data2Bots Assessment

## Schema Generator

This is the submission for the data2bot python engineer assessment. A schema generator is developed to parse a given json file to a schema description of the content.
Sample datasets are present in the **data** directory, and the equivalent parsed schema is present in the **schema** directory.
The program responsible for the generation of schema file is present in the **schema_generator** directory. It contains the Schema Data Types supported and a SchemaGenerator class which performs the parsing of data to schema.
The generated schema contains the data type of the attributes of the data and also go ahead to compute for where data is nested in an array or object. Therefore a summary structure of the schema is as followss:

```json
    {
        "key": {
            "type": data type of value for key,
            "tag": tag for the data,
            "description": description of data,
            "required": if data is required or not,
            "attrs": information about the data nested data in object or array
        }
    }
```

### Installation

1. A minimum of python 6 should be installed on target system
2. No external dependency is needed.

### Execution

A sample execution is present in main.py. Data present in the **data** directory is parsed into the **schema** directory.
Run the following to execute

```python
python main.py
```

### Tests

Run the following command to run tests

```python
python -m unittest
```
