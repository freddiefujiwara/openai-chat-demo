import openai
import os
openai.api_key = os.environ.get('OPENAI')
print(openai.api_key)
engines = openai.Engine.list()
print(engines)