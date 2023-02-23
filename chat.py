import openai

openai.api_key = ""
engines = openai.Engine.list()
print(engines)