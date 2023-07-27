import inspect
from langchain.prompts import StringPromptTemplate
from pydantic import BaseModel, validator

def get_source_code(function_name):
    # Get the source code of the function
    return inspect.getsource(function_name)
def get_source_code2(function_name):
    return inspect.getsource(function_name)+"2"


PROMPT = """\
Given the function name and source code, generate an English language explanation of the function.
Function Name: {function_name}
Source Code:
{source_code}
Explanation:
"""
class FunctionExplainerPromptTemplate(StringPromptTemplate, BaseModel):

    def format(self, **kwargs) -> str:
        source_code = get_source_code(kwargs["aaaa"])
        prompt = PROMPT.format(
            function_name=kwargs["aaaa"].__name__, source_code=source_code
        )
        return prompt

if __name__ == '__main__':
   # 传入一个function_name 的变量
   fn_explainer = FunctionExplainerPromptTemplate(input_variables=["aaaa"])

   #  调用FunctionExplainerPromptTemplate 的format方面，设置变量function_name=get_source_code
   prompt = fn_explainer.format(aaaa=get_source_code2)
   print(prompt)