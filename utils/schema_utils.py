import json
from jsonschema import validate, ValidationError

def load_schema(schema_file: str) -> dict:
    """
    Load a JSON schema from the schemas folder with UTF-8 encoding.
    """
    try:
        with open(f"schemas/{schema_file}", "r", encoding="utf-8") as f:
            schema = json.load(f)
        return schema
    except FileNotFoundError:
        raise FileNotFoundError(f"Schema file '{schema_file}' not found in 'schemas/' folder.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in schema file '{schema_file}': {e}")

def validate_schema(response_json: dict, schema_file: str):
    """
    Validate a JSON response against a schema.

    Raises AssertionError with helpful message if validation fails.
    """
    schema = load_schema(schema_file)

    try:
        validate(instance=response_json, schema=schema)
    except ValidationError as e:
        # Include the path in JSON where it failed
        path = ".".join(str(p) for p in e.absolute_path)
        path_msg = f" at '{path}'" if path else ""
        raise AssertionError(f"Schema validation failed{path_msg}: {e.message}") from e