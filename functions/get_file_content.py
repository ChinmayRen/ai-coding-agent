
import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory,file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: File"{file_path}" is not inside the working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" does not exist'
    
    file_content_string = ""
    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += (
                f'[...File: "{file_path}" truncated to "{MAX_CHARS}" characters...]'
                )
        return file_content_string
    
    except Exception as e:
        return f'Error: Failed to read file "{file_path}": {e}'
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the specified file and returns its contents, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to read, relative to the working directory.",
            ),
        },
    ),
)
    
# ...done...