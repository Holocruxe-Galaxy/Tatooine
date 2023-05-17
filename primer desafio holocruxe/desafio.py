import openai
import os
from datos import *

# pregunta1 = input()

# if "gusto" "gustar" in pregunta1:
#     print "hola"
# else:

# Configure la clave de la API de OpenAI
openai.api_key = "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"

pruegunta = input()
# Enviar una solicitud de prueba a la API de ChatGPT
prompt = pruegunta
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.7,
)