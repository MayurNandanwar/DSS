import json 

def get_current_weather(location, unit='fahrenheit'):
    """Get the current weather in given location"""

    weather_info = {
        "location":location,
        "temperature":"72",
        "unit":unit,
        "forecast":["sunny","windy"]
    }
    return json.dumps(weather_info)

messages = [
    {
        "role": "user",
        "content": "What's the weather like in Boston?"
    }
]

functions = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        },
    }
]

import openai
response = openai.ChatCompletion.create(
    # OpenAI Updates: As of June 2024, we are now using the GPT-3.5-Turbo model
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions
)

response = {
  "id": "chatcmpl-AVCsmqFCt4FILgYpy7wDxpjahOZvC",
  "object": "chat.completion",
  "created": 1732001052,
  "model": "gpt-3.5-turbo-0125",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": null,
        "function_call": {
          "name": "get_current_weather",
          "arguments": "{\"location\":\"Boston\",\"unit\":\"celsius\"}"
        },
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "function_call"
    }
  ],
  "usage": {
    "prompt_tokens": 82,
    "completion_tokens": 20,
    "total_tokens": 102,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "system_fingerprint": null
}

response_message = response["choices"][0]["message"]

json.loads(response_message["function_call"]["arguments"])

args = json.loads(response_message["function_call"]["arguments"])

tresult = get_current_weather(args)





messages = [
    {
        "role": "user",
        "content": "hi!",
    }
]

response = openai.ChatCompletion.create(
    # OpenAI Updates: As of June 2024, we are now using the GPT-3.5-Turbo model
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions,
)

response = {
  "id": "chatcmpl-AVD2kZpxzjjPkRdcYqPSH72DAQIgs",
  "object": "chat.completion",
  "created": 1732001670,
  "model": "gpt-3.5-turbo-0125",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I assist you today?",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 76,
    "completion_tokens": 10,
    "total_tokens": 86,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "system_fingerprint": null
}


#! Response of this 2 message we could know that model determines whether to call function 

#! there are the other params that force or not to use function 
messages = [
    {
        "role": "user",
        "content": "hi!",
    }
]
response = openai.ChatCompletion.create(
    # OpenAI Updates: As of June 2024, we are now using the GPT-3.5-Turbo model
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions,
    function_call="auto" #! auto let model decide  to call function or not default is 'auto',
)
print(response)

response = {
  "id": "chatcmpl-AVD2kZpxzjjPkRdcYqPSH72DAQIgs",
  "object": "chat.completion",
  "created": 1732001670,
  "model": "gpt-3.5-turbo-0125",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I assist you today?",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 76,
    "completion_tokens": 10,
    "total_tokens": 86,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "system_fingerprint": null
}



messages = [
    {
        "role": "user",
        "content": "hi!",
    }
]
response = openai.ChatCompletion.create(
    # OpenAI Updates: As of June 2024, we are now using the GPT-3.5-Turbo model
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions,
    function_call="none" #! this forces the LLM model not to use function,
)
print(response)

messages = [
    {
        "role": "user",
        "content": "What's the weather in Boston?",
    }
]
response = openai.ChatCompletion.create(
    # OpenAI Updates: As of June 2024, we are now using the GPT-3.5-Turbo model
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions,
    function_call="none",
)
print(response)
{
  "id": "chatcmpl-AVD7PzmAAhjBqgvw8V7vGP8A2k7D5",
  "object": "chat.completion",
  "created": 1732001959,
  "model": "gpt-3.5-turbo-0125",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "I can find out the weather in Boston for you. Should I display the temperature in Celsius or Fahrenheit?",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 82,
    "completion_tokens": 21,
    "total_tokens": 103,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "system_fingerprint": null
}


messages = [
    {
        "role": "user",
        "content": "What's the weather like in Boston!",
    }
]
response = openai.ChatCompletion.create(
    # OpenAI Updates: As of June 2024, we are now using the GPT-3.5-Turbo model
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions,
    function_call={"name": "get_current_weather"} #! forcing llm to call the function,
)
print(response)
{
  "id": "chatcmpl-AVDAAISqfQ0vGR1hIdwyVTBjMjcSX",
  "object": "chat.completion",
  "created": 1732002130,
  "model": "gpt-3.5-turbo-0125",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": null,
        "function_call": {
          "name": "get_current_weather",
          "arguments": "{\"location\":\"Boston\",\"unit\":\"celsius\"}"
        },
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 92,
    "completion_tokens": 10,
    "total_tokens": 102,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "system_fingerprint": null
}


messages = [
    {
        "role": "user",
        "content": "hi!",
    }
]
response = openai.ChatCompletion.create(
    # OpenAI Updates: As of June 2024, we are now using the GPT-3.5-Turbo model
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions,
    function_call={"name": "get_current_weather"},
)
print(response) #! here force to call function
{
  "id": "chatcmpl-BJuwfywMFU31LYj9iEebNnP3K07ce",
  "object": "chat.completion",
  "created": 1744086829,
  "model": "gpt-3.5-turbo-0125",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": null,
        "function_call": {
          "name": "get_current_weather",
          "arguments": "{\"location\":\"San Francisco\",\"unit\":\"celsius\"}"
        },
        "refusal": null,
        "annotations": []
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 86,
    "completion_tokens": 12,
    "total_tokens": 98,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": null
}


messages.append(response['choices'][0]['message'])
args = json.loads(response['choices'][0]['message']['function_call']['arguments'])

observation = get_current_weather(args)

messages.append([{'role':'function',
                 'name':'get_current_weather',
                 'context':observation}])

response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
    messages=messages)

print(response)




#! LCEL:
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

print(chain.invoke({"topic:bear"}))





#RAG
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import DocArrayInMemorySearch

vectorstore = DocArrayInMemorySearch.from_texts(['bear like to eat honey','harrison worked at kesho'])
retriver = vectorstore.as_retriever()

retriver.get_relevant_documents('what do bear likes to eat')

retriver.get_relevant_documents('where was harrison worked?')
                                

template = """Answer the question based on following context: {context} 
            Question:{question}
            """
prompt = ChatPromptTemplate.from_template(template)


from langchain.schema.runnable import RunnableMap

chain = RunnableMap({"context":lambda x: retriver.get_relevant_documents(x['question']),
             "question":lambda x: x['question']
             }) | prompt | model

chain.invoke({"question":"where did the harrison worked?"})





#! bind function with model

functions = [
    {
      "name": "weather_search",
      "description": "Search for weather given an airport code",
      "parameters": {
        "type": "object",
        "properties": {
          "airport_code": {
            "type": "string",
            "description": "The airport code to get the weather for"
          },
        },
        "required": ["airport_code"]
      }
    }
  ]

prompt = ChatPromptTemplate.from_messages([
                                          {"user":{input}}
                                          ])

model = ChatOpenAI(temperature=0)

model_with_function  = model.bind(functions=functions)

runnable = prompt | model_with_function

runnable.invoke({'input':"what is weather in sf?"})


#! add another function 
functions = [
    {
      "name": "weather_search",
      "description": "Search for weather given an airport code",
      "parameters": {
        "type": "object",
        "properties": {
          "airport_code": {
            "type": "string",
            "description": "The airport code to get the weather for"
          },
        },
        "required": ["airport_code"]
      }
    },
        {
      "name": "sports_search",
      "description": "Search for news of recent sport events",
      "parameters": {
        "type": "object",
        "properties": {
          "team_name": {
            "type": "string",
            "description": "The sports team to search for"
          },
        },
        "required": ["team_name"]
      }
    }
  ]

# update model by binding 2 function 
model = model.bind(functions=functions)

runnable = prompt | model

runnable.invoke({"input":"how did the sachin do yesterday?"})

#! here we get the AIResponse but i want in perticyular format like json , string so we can attach fallback not only to 
#! indevidual component but entire sequences
#! older version of llm fails to provide answer in requred format like json 
#! new model in open ai is good for that 


from langchain.llms import OpenAI
import json

simple_model = OpenAI(temperature=0,
                      max_token=1000,
                      model = 'text-davinci-001')

simple_chain = simple_model | json.loads

challange = "write poem in a json blob,where each poem is a json blob of title,author and first line"

simple_chain.invoke("write poem in a json blob,where each poem is a json blob of title,author and first line")
# using above here got error 

#! with new model
model = ChatOpenAI(temperature=0)
chain = model | StrOutputParser() | json.loads

chain.invoke(challange)

# we get the json result

#! InORder to use fallback
final_chain = simple_chain.with_fallbacks([chain]) # this says if simple_chain raise error the go through list here only one chain(or runnable) is there but multiple(chain or runnable) possible 

final_chain.invoke(challange)

#! main goal is try on simpler model or simple chain and if rais error the go with other good chain.


#! methods : invoke , batch , stream # synchronus method
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

print(chain.invoke({"topic:bear"}))

print(chain.batch([{"topic":"bear"},{"topic":"cat"}]))

for t in chain.stream({"topic":"bear"}) # this is very usefull because llm model sometimes take a while so streaming output is usefull:
    print(t)

#! all this method has asynchronus version 
response = await chain.ainvoke({"topic":"bear"})




#! use function with LLM 
from typing import List
from pydentic import BaseModel,Field

class pUser(BaseModel):
    name :str
    age : int

class_obj = pUser(name='mayur',age=32)


class Class(BaseModel):
    students:List[pUser]

obj = Class(students = [pUser(name='mayur',age=32)])

print(obj)
#--> Class(students=[pUser(name='mayur',age=32)])


#! how to use pydentic to create openai functions

class WeatherSearch(BaseModel):
    """Call this with an airport code to get the weather at that airport"""
    airport_code: str = Field(description="airport code to get weather for")

from langchain.utils.openai_functions import convert_pydantic_to_openai_function

weather_function = convert_pydantic_to_openai_function(WeatherSearch)
#! weather_function is json schema that we pass into openAI model
#! class description is very very important if you do not provide the get description error 
#! to provide description to arguments of class is not necessary 

class WeatherSearch(BaseModel):
    airport_code: str = Field(description="airport code to get weather for")

from langchain.utils.openai_functions import convert_pydantic_to_openai_function

weather_function = convert_pydantic_to_openai_function(WeatherSearch)
print(weather_function)
#! -->gives Error

class WeatherSearch(BaseModel):
    """Call this with an airport code to get the weather at that airport"""
    airport_code: str 

from langchain.utils.openai_functions import convert_pydantic_to_openai_function

weather_function = convert_pydantic_to_openai_function(WeatherSearch)
print(weather_function) 
#! this will work


from langchain.chat_models import ChatOpenAI
model = ChatOpenAI()

model.invoke("what is the weather in sf?",functions=[weather_function])
#! if we do not want to pass args inside invoke 

model_with_function = model.bind(functions=[weather_function])

model_with_function.invoke('what is weather in sf?')
#! if you want to force to call the function every time 
model_with_forced_function = model.bind(functions=[weather_function],function_call = {"name":"WeatherSearch"})

model_with_forced_function.invoke("what is weather in sf?")


#! use with prompt
from langchain.prompts import ChatPromptTemplate 

prompt = ChatPromptTemplate.from_message([
    ('system',"you are a helpful assistant"),
    ('user',"{input}")
])

chain = prompt | model_with_function

chain.invoke({"input":"what is the weather is sf?"})

#! we can also pass list of function and let model decide which to use

class ArtistSearch(BaseModel):
    "Call this to get the name of song by perticulat artist"
    artist_name:str = Field(description="name of the artist to lookup")
    n:int = Field(description="number of result")

function_list = [
                  convert_pydantic_to_openai_function(WeatherSearch),
                  convert_pydantic_to_openai_function(ArtistSearch)
                ]

model_with_function = model.bind(functions=function_list)

model_with_function.invoke('what is weather in sf ?')

model_with_function.invoke('what are three song by tailor swift ?')

#! here we not force the model every time to use functions
model_with_function.invoke('hii')
#--> model_res = How can i assist you?


#!!!! Tagging 
#--> given input is postive or negative sentiment we just have to tag
# Llm from given function description, select arguments from the input text generate structured output forming a function call
# more generally , LLm evaluate input text and generate the structured output
# ex. look at the artical and mension all the paper and its author

class Tagging(BaseModel):
    "Tag the piece of text with perticular information."
    sentiment: str = Field("sentiment of text, should be `positive`, `negative` , or `neutral` ")
    sentiment: str = Field(description="sentiment of text, should be `pos`, `neg`, or `neutral`")
    language: str = Field(description="language of text")

tagging_function = convert_pydantic_to_openai_function(Tagging)
#
{'name': 'Tagging',
 'description': 'Tag the piece of text with particular info.',
 'parameters': {'title': 'Tagging',
  'description': 'Tag the piece of text with particular info.',
  'type': 'object',
  'properties': {'sentiment': {'title': 'Sentiment',
    'description': 'sentiment of text, should be `pos`, `neg`, or `neutral`',
    'type': 'string'},
   'language': {'title': 'Language',
    'description': 'language of text (should be ISO 639-1 code)',
    'type': 'string'}},
  'required': ['sentiment', 'language']}}

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

model = ChatOpenAI(temperature=0)
prompt = ChatPromptTemplate.from_messages([
    ("system","think carefully and then tag the text as instructed")
    ("user","{input}")
      ])

model_with_function = model.bind(functions=[tagging_function],function_call={"name":"Tagging"})

tagging_chain = prompt | model_with_function

tagging_chain.invoke({'input':'i love langchain'})
#--> ans : AIMessage(content='', additional_kwargs={'function_call': {'name': 'Tagging', 'arguments': '{"sentiment":"pos","language":"en"}'}})
tagging_chain.invoke({"input": "non mi piace questo cibo"})
#--> ans : AIMessage(content='', additional_kwargs={'function_call': {'name': 'Tagging', 'arguments': '{"sentiment":"neg","language":"it"}'}})

from langchain.output_parsers.openai_functions import JsonKeyOutputFunctionsParser

tagging_chain = prompt | model_with_function | JsonKeyOutputFunctionsParser()

tagging_chain.invoke({"input": "non mi piace questo cibo"})
#--> {'sentiment': 'neg', 'language': 'it'}



#!!!!! Extraction :  here we extract the pieces of information 

from typing import Optional
class Person(BaseModel):
    "Information about person"
    name:str = Field(description="Person's name") 
    age:Optional[int] = Field(description="Person's age")

class Information(BaseModel):
    people:List[Person] = Field(description='List of information about people.')

extraction_function = convert_pydantic_to_openai_function(Information)

extraction_model = model.bind(functions=[extraction_function],function_call={"name":"Information"})

extraction_model.invoke("Joe is 30 year old and his mom is Martha.")
#--> ans:AIMessage(content='', additional_kwargs={'function_call': {'name': 'Information', 'arguments': '{"people":[{"name":"Joe","age":30},{"name":"Martha","age":0}]}'}})
# here age of marth 0 given by model because text does not contain this.

prompt = ChatPromptTemplate.from_messages([
    ("system","extract the information available from text and if not explicitely available do not guess"),
    ("human","{input}")])

extraction_chain = prompt | extraction_model

extraction_model.invoke("Joe is 30 year old and his mom is Martha.")
#--> AIMessage(content='', additional_kwargs={'function_call': {'name': 'Information', 'arguments': '{"people":[{"name":"Joe","age":30},{"name":"Martha"}]}'}})

extraction_chain = prompt | extraction_model | JsonKeyOutputFunctionsParser()

extraction_chain.invoke({"input": "Joe is 30, his mom is Martha"})
#-->{'people': [{'name': 'Joe', 'age': 30}, {'name': 'Martha'}]}

extraction_chain = prompt | extraction_model | JsonKeyOutputFunctionsParser(key_name="people")
extraction_chain.invoke({"input": "Joe is 30, his mom is Martha"})
# --> [{'name': 'Joe', 'age': 30}, {'name': 'Martha'}]



#! laod blog post and extract information from that
from langchain.document_loaders import WebBaseLoader
loader = WebBaseLoader('https://lilianweng.github.io/posts/2023-06-23-agent/')
documents = loader.load()
doc = documents[0]
page_content = doc.page_content[:10000]


class Overview(BaseModel):
    """Overview of a section of text."""
    summary: str = Field(description="Provide a concise summary of the content.")
    language: str = Field(description="Provide the language that the content is written in.")
    keywords: str = Field(description="Provide keywords related to the content.")


overview_tagging_function = [
    convert_pydantic_to_openai_function(Overview)
]
tagging_model = model.bind(
    functions=overview_tagging_function,
    function_call={"name":"Overview"}
)
tagging_chain = prompt | tagging_model | JsonKeyOutputFunctionsParser()

tagging_chain.invoke({"input": page_content})
#--> ans : {'summary': 'The article discusses building autonomous agents powered by LLM (large language model) as the core controller. It covers components like planning, memory, and tool use, along with challenges and case studies.',
# 'language': 'English',
# 'keywords': 'LLM, autonomous agents, planning, memory, tool use, challenges, case studies'}





#! extract paper and auther from it 

class Paper(BaseModel):
    '''Extract information about papers mensioned'''
    title:str = Field(description='name of the paper')
    author:Optional[str] = Field(description='paper published by auther')

class Infomation(BaseModel):
    """Information to extract"""
    papers:List[Paper] = Field(description='Information about paper')


extract_paper_function = convert_pydantic_to_openai_function(Information)

template = """A article will be passed to you. Extract from it all papers that are mentioned by this article follow by its author. 

Do not extract the name of the article itself. If no papers are mentioned that's fine - you don't need to extract any! Just return an empty list.

Do not make up or guess ANY extra information. Only extract what exactly is in the text."""

prompt = ChatPromptTemplate.from_messages([
    ("system",template)
    ("user","{input}")
])

extract_paper_model = model.bind(functions=[extract_paper_function],function_call={'name':'Infomation'})

extraction_chain = prompt | extract_paper_model | JsonKeyOutputFunctionsParser(key_name="papers")

extraction_chain.invoke({"input": page_content})

# ==> ans:[{'title': 'Chain of thought (CoT; Wei et al. 2022)'},
          # {'title': 'Tree of Thoughts (Yao et al. 2023)'},
          # {'title': 'LLM+P (Liu et al. 2023)'},
          # {'title': 'ReAct (Yao et al. 2023)'},
          # {'title': 'Reflexion (Shinn & Labash 2023)'},
          # {'title': 'Chain of Hindsight (CoH; Liu et al. 2023)'},
          # {'title': 'Algorithm Distillation (AD; Laskin et al. 2023)'}]


extraction_chain.invoke({"input": "hi"})
#==> ans: []



from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_overlap=100)

splits = text_splitter.split_text(doc.page_content)
len(splits)


def flatten(matrix):
    flat_list = []
    for row in matrix:
        flat_list += row
    return flat_list

from langchain.schema.runnable import RunnableLambda

prep = RunnableLambda(
    lambda x: [{"input": doc} for doc in text_splitter.split_text(x)]
)

prep.invoke("hi")

chain = prep | extraction_chain.map() | flatten   #extraction_chain.map() : used when we have list of input # when i pass doc.page_content to the 'prep' then i will get list of dictionary [{'input':'content'},{'input':'content'}]

chain.invoke(doc.page_content) 