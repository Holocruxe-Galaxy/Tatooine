# import openai
# import os
# from datos import *

# ask a question
tema_comida = ["comida","comidas","comer"]

pregunta = input("Dime")

if pregunta.lower() in tema_comida:
    print("me gusta el queso")
else:
    print("no entiendo la pregunta.")






# # Configure la clave de la API de OpenAI
# openai.api_key = "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"

# pruegunta = input()
# # Enviar una solicitud de prueba a la API de ChatGPT
# prompt = pruegunta
# response = openai.Completion.create(
#     engine="davinci",
#     prompt=prompt,
#     max_tokens=100,
#     n=1,
#     stop=None,
#     temperature=0.7,
# )