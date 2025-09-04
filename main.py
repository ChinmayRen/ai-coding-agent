import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import call_function, available_functions


def main():
    

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    system_prompt = """
    You are a helpful AI coding agent.
    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files
    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    verbose_flag = False

    if len(sys.argv) < 2:
        print("I need a prompt as an argument")
        sys.exit(1)

    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        print("Verbose mode on")
        verbose_flag = True

    prompt = sys.argv[1]

    messages = [
        types.Content(role = "user", parts = [types.Part(text = prompt)]),
        ]
    
    

    config = types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
 
    max_iters = 20
    for i in range(max_iters):
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents = messages,
            config=config,
            )
        
        if response.usage_metadata is None or response is None:
            print("No response from the model")

        if verbose_flag:
            print(f"User Prompt: {prompt}")
            print("Prompt Tokens:", response.usage_metadata.prompt_token_count)
            print("Response Tokens:", response.usage_metadata.candidates_token_count)

    
        if response.candidates:
            for candidate in response.candidates:
                if candidate is None or candidate.content is None:
                    continue
                messages.append(candidate.content)

        if response.function_calls:
            for function_call_part in response.function_calls:
                result = call_function(function_call_part, verbose=verbose_flag)
                messages.append(result)
        else:
            print(response.text)
            return

    # function_responses = []
    # for function_call_part in response.function_calls:
    #     function_call_result = call_function(function_call_part, verbose=verbose_flag)
    #     if (
    #         not function_call_result.parts
    #         or not function_call_result.parts[0].function_response
    #     ):
    #         raise Exception("empty function call result")
    #     if verbose_flag:
    #         print(f"-> {function_call_result.parts[0].function_response.response}")
    #     function_responses.append(function_call_result.parts[0])

    # if not function_responses:
    #     raise Exception("no function responses generated, exiting.")
    

main()