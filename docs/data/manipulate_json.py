import json

flare_type_empty_list = []
with open('vega/docs/data/heirarchy_data.json') as f:
    root = json.load(f)
    flare_type_parent_child = []
    flare_type_dependencies = []
    id = 1
    flare_type_parent_child.append({
        "id": id,
        "name": root["name"],
    })
    children = [(id, x) for x in root["children"]]
    id += 1
    while children:
        parent_id, child = children.pop()
        flare_type_parent_child.append({
            "id": id,
            "name": child["name"],
            "parent": parent_id
        })
        if child.get("children"):
            children += [(id, x) for x in child["children"]]
        id += 1

print(flare_type_parent_child)
with open("vega/docs/data/heirarchy_data_mod.json", "w") as f:
    json.dump(flare_type_parent_child, f)

# Create dependencies file
ids = [x['id'] for x in flare_type_parent_child]
count = 0
while count < 10:
    a = random.choice(flare_type_parent_child)
    b = random.choice(flare_type_parent_child)
    if a["parent"] != b["id"] and a["id"] != b["parent"] and a["id"] != b["id"]:
        flare_type_dependencies.append({"source": a["id"], "target": b["id"]})
        count += 1

with open("vega/docs/data/heirarchy_data_dep.json", "w") as f:
    json.dump(flare_type_dependencies, f)
