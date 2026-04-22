import json
from collections import defaultdict

data = json.load(open("mark6_history.json"))

# ------------------------
# 五行映射
# ------------------------
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

# ------------------------
# ① 时间衰减权重
# ------------------------
def time_weight(i, total):
    return 1 / (total - i + 1)


# ------------------------
# ② 热度统计
# ------------------------
hot = defaultdict(int)

# ------------------------
# ③ 特别号周期
# ------------------------
special_gap = defaultdict(list)
last_seen = {}

for i,d in enumerate(data):

    for n in d["main"]:
        hot[n] += 1

    sp = d["special"]

    if sp in last_seen:
        special_gap[sp].append(i - last_seen[sp])

    last_seen[sp] = i


# 平均周期
avg_cycle = {}

for k,v in special_gap.items():

    if len(v)>0:
        avg_cycle[k] = sum(v)/len(v)


# ------------------------
# AI评分函数
# ------------------------
def score(item, i, total):

    main = item["main"]
    sp = item["special"]

    s = 0

    # 五行
    for n in main:

        e = ele(n)

        if e in ["火","木"]:
            s += 2

        if e in ["金","水"]:
            s += 1

    # 热度
    for n in main:
        s += hot[n] * 0.05

    # 冷号补偿
    for n in range(1,50):
        if hot[n] == 0:
            s += 0.1

    # 时间衰减
    s *= time_weight(i,total)

    # 特别号周期匹配
    if sp in avg_cycle:

        expected = avg_cycle[sp]

        gap = total - last_seen[sp]

        diff = abs(gap - expected)

        s += max(0, 5 - diff*0.2)

    return s


# ------------------------
# 评分所有数据
# ------------------------
scored = []

for i,d in enumerate(data):

    s = score(d,i,len(data))

    scored.append((d["main"],d["special"],s))


scored.sort(key=lambda x:-x[2])


# ------------------------
# 输出
# ------------------------
with open("mark6_ai.txt","w") as f:

    for m,s,sc in scored[:12]:

        f.write(
            " ".join(f"{x:02d}" for x in m)
            + " + "
            + f"{s:02d}"
            + f" #AI4.0:{round(sc,2)}\n"
        )

print("AI4.0 done")