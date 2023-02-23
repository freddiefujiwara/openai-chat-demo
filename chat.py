"""
This code is an example of how to use the OpenAI Python module.
"""
import os
import openai
openai.api_key = os.environ.get('OPENAI_KEY')
engines = openai.Engine.list()
print(engines)
