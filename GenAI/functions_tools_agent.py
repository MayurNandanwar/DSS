
#! how LLM intract with the software infrastructure ex. by let it decide to make a function call to different programme to get the information or to take action
#! generally llm is train to get the text the data but now llm have been train to output the json format let the llm to call other function or programm.
#! ex. with the help of function,tools, let llm helps to extract the structured information from tabular data which llm have struggle with it.

#! (LCEL: Langchain expression language): this makes composing component or chain simpler and more intuative.
#! function calling : helps to exctract data, tagging. function calling makes building tools for LLM simpler and more reliable.
#! we build the tool and use them to build conversational agent, Agent can do complex and multi-step reasoning and select tool to help to solve complex problem.



#! Function Calling:
#! --> # define a function
# functions = [
#     {
#         "name": "get_current_weather",
#         #! "description": "Get the current weather in a given location",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "location": {
#                     "type": "string",
#                     #!"description": "The city and state, e.g. San Francisco, CA",
#                 },
#                 "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
#             },
#             "required": ["location"],
#         },
#     }
# ]

#! here descriptions are very important which are going to pass directly to llm and llm use this function to determine whether to use function 
#! whether to call a function, model will know with the help of this given descriptions.

#! 3 params model to call function , to take decision to call function or not to call function 
    #! 1) function_call = 'auto': LLM take decision to call function.
    #! 2) function_call = 'none': force llm to not call function 
    #! 3) function_call = {"name": "get_current_weather"} : force llm to call function.

#! function themselves and description count against the token limit that you pass to ai because llm hs token limit
#! this thing need to know because when you pass the question to the llm model and llm model call the function and 
#! again pass this result information back to LLM so this thing is important



#! LCEL (Langchain Expression Language) #* 
#!@ advantage
#! Clean and declarative syntax – Makes it easier to build and understand complex chains.you get async batch and streaming support
#! big part working with LLMs, they dont respond always what you want them to respond so you can easily attach the fallback not only llm but also to chain
#! parralleism : llm calls can be time consuming. they oftern take a while. it important to run them parallel and LCEL syntex makes it easy to do it
#! loging built in : as agent and chain get more and more compex beinng able to see sequence of step input and output become crutial for llm application. we have Langsmit opensource plat form for logging and debugging platform
# this allows set of input types and corrosponding output type ex. json string

#! pydentic library help to construct the functions. it is data validation library for python
# langchain leverages pydantic to create json schema describing functuion  
#! validation Library means
#ex.


class user:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age

# obj = user(name='mayur',age=39)
# print(obj.age)
#! when we change value of age from int to string 
obj = user(name='mayur',age='aaa')
print(obj.age) # python does not validate the type but pydentic valiate this things





