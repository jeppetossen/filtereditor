import json


def fetch_header():
    file = "editor/modules/content/headers.json"
    with open(file, "r") as f:
        data = json.load(f)
        f.close()

    return data
