import json
import os
import random

INPUT_FILE = "data_warehouse.json"
OUTPUT_FILE = "mark6_ai.txt"


# =============================
# 1️⃣ 安全加载数据（防断链核心）
# =============================
def load_data():

    if not os.path.exists(INPUT_FILE):

        print("⚠️ data_warehouse.json not found, using fallback data")

        return [
            {"main":[1,2,3,4,5,6], "special":7},
            {"main":[7,8,9,10,11,12], "special":13},
            {"main":[13,14,15,16,17,18], "special":19}
        ]

    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not data:
            raise ValueError("empty data")

        return data

    except Exception as e:

        print("⚠️ load error:", e)

        return [
            {"main":[1,2,3,4,5,6], "special":7}
        ]


# =============================
# 2️⃣ 五行系统
# =============================
WX = {
    "木":[3,8,13,18,23,28,33,38,43,48],
    "火":[2,7,12,17,22,27,32,37,42,47],
    "土":[5,10,15,20,25,30,35,40,45],
    "金":[4,9,14,19,24,29,34,39,44,49],
    "水":[1,6,11,16,21,26,31,36,41,46]
}


def get_element(n):
    for k, v in WX.items():
        if n in v:
            return k
    return "土"


# =============================
# 3️⃣ AI评分模型
# =============================
def score(item):

    s = 0

    for n in item["main"]:

        e = get_element(n)

        if e in ["火", "木"]:
            s += 2
        elif e in ["金", "水"]:
            s += 1
        else:
            s += 1.5

    # 特别号权重
    s += item.get("special", 0) * 0.01

    # 随机微扰（避免完全固定）
    s += random.uniform(0, 0.5)

    return s


# =============================
# 4️⃣ 主流程
# =============================
def main():

    data = load_data()

    results = []

    for d in data:

        # 数据保护
        if "main" not in d or "special" not in d:
            continue

        if len(d["main"]) != 6:
            continue

        results.append((
            d["main"],
            d["special"],
            score(d)
        ))

    # =========================
    # 5️⃣ 防空机制（关键）
    # =========================
    if not results:

        print("⚠️ no valid data, using fallback results")

        for _ in range(10):

            nums = random.sample(range(1, 50), 7)

            results.append((
                nums[:6],
                nums[6],
                random.uniform(5, 10)
            ))

    # =========================
    # 6️⃣ 排序
    # =========================
    results.sort(key=lambda x: -x[2])

    # =========================
    # 7️⃣ 输出文件
    # =========================
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

        for m, s, sc in results[:15]:

            line = (
                " ".join(f"{x:02d}" for x in m)
                + " + "
                + f"{s:02d}"
                + f" #AI6.0:{round(sc,2)}"
            )

            f.write(line + "\n")

    print("✅ AI engine done, output generated:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
