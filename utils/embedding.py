# import requests
# import numpy as np
# import os

# API_KEY = os.getenv("EURI_API_KEY")

# def get_embedding(text, model="text-embedding-3-small"):
#     url = "https://api.euron.one/api/v1/euri/embeddings"

#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "input": text,
#         "model": model
#     }

#     response = requests.post(url, headers=headers, json=payload)
#     return np.array(response.json()["data"][0]["embedding"])

#     print("Status Code:", response.status_code)

#     data = response.json()
#     print("Response:", data)

#     if "data" not in data:
#         raise Exception(f"Unexpected API response: {data}")

#     return np.array(data["data"][0]["embedding"])

import requests
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EURI_API_KEY")


def get_embedding(text, model="text-embedding-3-small"):

    if not API_KEY:
        raise ValueError("EURI_API_KEY not found")

    url = "https://api.euron.one/api/v1/euri/embeddings"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "input": text,
        "model": model
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    return np.array(
        data["data"][0]["embedding"]
    )