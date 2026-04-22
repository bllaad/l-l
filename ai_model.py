import json

data = json.load(open("data_warehouse.json"))


WX = {
"木":[3,8,13,18,23,28,33,38,43,48],
"火":[2,7,12,17,22,27,32,37,42,47],
"土":[5,10,15,20,25,30,35,40,45],
"金":[4,9,14,19,24,29,34,39,44,49],
"水":[1,6,11,16,21,26,31,36,41,46]
}


def ele(n):
    for k,v in WX.items():
        if n in v:
            return k


def score(d):

    s = 0

    for n in d["main"]:

        e = ele(n)

        s += 2 if e in ["火","木"] else 1

    # 稳定权重（AI6.0核心）
    s += d["special"] * 0.01

    return s


results = []

for d in data:

    results.append((d["main"], d["special"], score(d)))


results.sort(key=lambda x:-x[2])


with open("mark6_ai.txt","w") as f:

    for m,s,sc in results[:15]:

        f.write(
            " ".join(f"{x:02d}" for x in m)
            + " + "
            + f"{s:02d}"
            + f" #AI6.0:{round(sc,2)}\n"
        )

print("✅ AI6.0 engine done")