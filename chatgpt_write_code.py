import openai
import inspect
from functools import wraps

openai.api_key = "apikey"

def generate_code(func, docstring):
    init_prompt = "You are a Python expert who can implement the given function."
    definition = f"def {func}"
    prompt = f"Read this incomplete Python code:\n```python\n{definition}\n```"
    prompt += "\n"
    prompt += f"Complete the Python code that follows this instruction: '{docstring}'. Your response must start with code block '```python'."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=1024,
        top_p=1,
        messages=[
            {
                "role": "system",
                "content": init_prompt,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    codeblock = response.choices[0].message.content
    code = next(filter(None, codeblock.split("```python"))).rsplit("```", 1)[0]
    code = code.strip()

    return code


def chatgpt_code(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        signature = f'{func.__name__}({", ".join(inspect.signature(func).parameters)}):'
        docstring = func.__doc__.strip()
        code = generate_code(signature, docstring)
        print(f"generated code:\n```python\n{code}\n```")
        exec(code)
        return locals()[func.__name__](*args, **kwargs)

    return wrapper


if __name__ == '__main__':
    
    @chatgpt_code
    def bloom(target:str,storage:list):
        """
        Use a Bloom filter to check if the target is in storage , Just use this func , no more class
        """

    print(bloom("你好",["你好","Helloworld"]))
