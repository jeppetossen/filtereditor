import json


def load_headers():
    # file = "editor/modules/headers/testing.json"
    file = "testing.json"
    with open(file, "r") as f:
        data = json.load(f)
        f.close()

    return data


def get_sections():
    data = load_headers()
    section_names = list()
    for item in data:
        # sections.append(item)
        for prop in data[item]:
            if prop == "name":
                section_names.append(data[item]["name"])

    return section_names


def get_subsections():
    data = load_headers()
    subsection_names = list()
    for item in data:
        for section_prop in data[item]:
            for subsection in data[item]["Subsections"]:
                for subsection_name in data[item]["Subsections"][subsection]:
                    if subsection_name == "name":
                        subsection_names.append(data[item]["Subsections"][subsection][subsection_name])

    return subsection_names


if __name__ == '__main__':
    print(test())
    # print(get_sections())
    #print(len(get_subsections()))
    # print(retrieve_header_id())
    # print(str(len(retrieve_header_id()[1])))
