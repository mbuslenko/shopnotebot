import requests


REQUEST_URL = "http://127.0.0.1:8000/api/profile/"


def create_profile(external_id, name):
    payload = {"external_id": f"{external_id}", "name": f"{name}"}

    r = requests.post(
        REQUEST_URL,
        data=payload
    )
