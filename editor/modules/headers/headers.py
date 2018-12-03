import json


def load_headers():
    file = "editor/modules/headers/sections.json"
    # file = "headers.json"
    with open(file, "r") as f:
        data = json.load(f)
        f.close()

    return data


def get_sections():
    data = load_headers()
    sections = list()
    for item in data['Sections']:
        for section in data['Sections'][item]:
            if section == "name":
                sections.append(data['Sections'][item][section])

    return sections


def get_subsections():
    pass


if __name__ == '__main__':
    print(get_sections())
    # print(retrieve_header_id())
    # print(str(len(retrieve_header_id()[1])))
