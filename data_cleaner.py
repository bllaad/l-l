import json

def clean(data):

    clean_data = []

    for d in data:

        # ❗结构检查
        if "main" not in d or "special" not in d:
            continue

        # ❗长度检查
        if len(d["main"]) != 6:
            continue

        # ❗范围检查
        if any(n < 1 or n > 49 for n in d["main"]):
            continue

        if d["special"] < 1 or d["special"] > 49:
            continue

        clean_data.append(d)

    return clean_data


if __name__ == "__main__":

    raw = json.load(open("data_raw.json"))

    clean_data = clean(raw)

    json.dump(clean_data, open("data_warehouse.json","w"), indent=2)

    print("✅ data cleaned")