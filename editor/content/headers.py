import json


def fetch_header():
    file = "editor/content/headers.json"
    with open(file, "r") as f:
        data = json.load(f)
        f.close()

    return data
