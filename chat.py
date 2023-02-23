import openai
import os
openai.api_key = os.environ.get('OPENAI_KEY')
engines = openai.Engine.list()
print(engines)