import requests

url = "http://127.0.0.1:8000/process"

data = {
    "request_id": "test1",
    "income": 40000,
    "credit_score": 700
}

response = requests.post(url, json=data)

print(response.json())
