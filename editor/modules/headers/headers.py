import json


def fetch_header():
    file = "editor/modules/headers/headers.json"
    # file = "headers.json"
    with open(file, "r") as f:
        data = json.load(f)
        f.close()

    return data


def retrieve_header_id():
    headers = fetch_header()
    header_keys = list()
    for section, header in headers.items():
        for title, subheader in header.items():
            for block, item in subheader.items():
                try:
                    header_keys.append(item['id'])
                    # header_keys.append(subheader)
                except KeyError:
                    return "Failed to retrieve id."

    return header_keys


if __name__ == '__main__':
    print(retrieve_header_id())
