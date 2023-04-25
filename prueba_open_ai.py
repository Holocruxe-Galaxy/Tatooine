import openai
import json

openai.api_key = "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" # Reemplaza "API_KEY" con tu clave de API de OpenAI

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002", # Puedes cambiar "davinci" por el nombre de otro motor si lo deseas
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    message = response.choices[0].text.strip()
    return message

# Ejemplo de uso:
prompt = "¿Cuáles son las características de un buen líder?"
profesion= input()
response = chat_with_gpt(prompt)
print(response)
