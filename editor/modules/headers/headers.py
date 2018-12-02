import json


def load_headers():
    file = "editor/modules/headers/headers.json"
    # file = "headers.json"
    with open(file, "r") as f:
        data = json.load(f)
        f.close()

    return data


def retrieve_header_id():
    headings = load_headers()
    sections = dict()
    subsections = dict()
    blocks = dict()
    tier_keys = dict()

    i = 0
    k = 0
    v = 0
    n = 0
    for section, headers in headings.items():
        i += 1
        sections[section] = i
        for subsection, tiers in headers.items():
            k += 1
            subsections[subsection] = i
            for tier, items in tiers.items():
                v += 1
                blocks[tier] = i
                for x, z in items.items():
                    try:
                        n += 1
                        tier_keys[x] = i
                    except KeyError:
                        return "Failed to retrieve id."
    return f"Sections: {sections}\nSubsections: {subsections}\nBlocks: {blocks}\nID's: {tier_keys}"

    # return sections, subsections, blocks, tier_keys


def get_subsection_id():
    headings = load_headers()
    names = list()
    numbers = list()

    for section, section_items in headings.items():
        for subsection, subsection_items in section_items.items():
            names.append(section)

    for i in range(1, len(names)+1):
        numbers.append(i)

    return numbers


if __name__ == '__main__':
    print(get_subsection_id())
    # print(retrieve_header_id())
    # print(str(len(retrieve_header_id()[1])))
