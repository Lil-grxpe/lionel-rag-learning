import os
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from groq import Groq

# 1. Charger la variable d'environnement depuis le fichier .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ Erreur : GROQ_API_KEY est absente de ton fichier .env")
    exit(1)

# 2. Initialiser le client Groq officiel
client = Groq(api_key=api_key)

# 3. Envoyer un message de test simple
print("Connexion à Groq Cloud en cours...")

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "user", "content": "Dis simplement Bonjour en une phrase !"}
    ]
)

# 4. Afficher la réponse
print("Réponse de Groq :")
print(response.choices[0].message.content)
