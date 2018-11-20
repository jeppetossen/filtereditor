import json


def fetch_header():
    # file = "editor/modules/content/headers.json"
    file = "headers.json"
    with open(file, "r") as f:
        data = json.load(f)
        f.close()

    return data


def create_headers_table():
    headers = fetch_header()
    for section, header in headers.items():
        for title, subheader in header.items():
            for block, item in subheader.items():
                print(item)


if __name__ == '__main__':
    create_headers_table()
