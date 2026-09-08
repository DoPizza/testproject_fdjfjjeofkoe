import requests

response = requests.post(
    "https://fangdenim-lwsvow.stormkit.dev/api/add-event",
    json={"title": "routing test"},
    timeout=15
)

print("STATUS:", response.status_code)
print("TYPE:", response.headers.get("Content-Type"))
print("BODY:", response.text)
