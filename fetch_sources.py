import json

def fetch_source_a():
    # 官方网页（模拟）
    return []

def fetch_source_b():
    # 历史库备用
    return []


def merge(a,b):

    return a if len(a)>len(b) else b


if __name__ == "__main__":

    a = fetch_source_a()
    b = fetch_source_b()

    data = merge(a,b)

    json.dump(data, open("data_raw.json","w"))

    print("✅ merged data")