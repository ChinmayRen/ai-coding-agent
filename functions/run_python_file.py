import os
import subprocess
from google.genai import types

def run_python_file(working_directory: str, file_path: str, args = []):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: File"{file_path}" is not inside the working directory' 
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" does not exist'
    if not file_path.endswith(".py"):
        return f'Error: File "{file_path}" is not a python file'
    
    try:
        final_args = ["python", file_path]
        final_args.extend(args)
        output = subprocess.run(
            final_args,
            cwd=abs_working_dir,
            capture_output=True,
            encoding='utf-8',
            errors='replace',
            timeout=30
        )
        finals_string =  f""" 
        STDOUT:\n{output.stdout}\n
        STDERR:\n{output.stderr}\n
        """

        if output.returncode != 0:
            finals_string += f"Process exited with code {output.returncode}"
        if output.stdout == b'' and output.stderr == b'':
            finals_string += "No output from the script.\n"
        return finals_string
        
    except Exception as e:
        return f'Error: Failed to run python file "{file_path}": {e}'
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the specified python file with Python interpreter and returns its output, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the python file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="The arguments to pass to the python file.",
                items=types.Schema(
                    type=types.Type.STRING,
                ),
            ),
        },
    ),
)
    
# ...done...