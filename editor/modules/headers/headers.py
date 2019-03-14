import json


def load_headers():
    file = "editor/modules/headers/old_headers.json"
    # file = "headers.json"
    with open(file, "r") as f:
        data = json.load(f)
        f.close()

    return data


def get_sections():
    data = load_headers()
    section_names = list()
    for k in data:
        section_names.append(k["name"])

    return section_names


def get_subsections():
    data = load_headers()
    subsection_names = list()
    for k in data["Sections"]:
        for v in k["Subsections"]:
            subsection_names.append(v["name"])
    return subsection_names


def get_block_sections():
    data = load_headers()
    blocksection_names = list()
    for k in data["Sections"]:
        for v in k["Subsections"]:
            if v["editor"] == "False":
                for h in v["BlockSections"]:
                    blocksection_names.append([h["name"], h["id"]])
    return blocksection_names


def get_blocks():
    data = load_headers()
    blocks = {"name": list(), "id": list()}
    for k in data["Sections"]:
        for v in k["Subsections"]:
            if v["editor"] == "True":
                for l in v["Blocks"]:
                    blocks["name"] += [l["name"]]
                    blocks["id"] += [l["id"]]
                    pass
            elif v["editor"] == "False":
                for j in v["BlockSections"]:
                    for h in j["Blocks"]:
                        blocks["name"] += [h["name"]]
                        blocks["id"] += [h["id"]]

    return blocks


if __name__ == '__main__':
    # print(load_headers())
    # print(get_sections())
    # print(get_subsections())
    # print(get_block_sections())
    print(get_blocks())
