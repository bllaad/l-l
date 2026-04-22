import json
import requests
from bs4 import BeautifulSoup

URL = "https://bet.hkjc.com/marksix/results"

def fetch():

    print("📡 fetching data...")

    html = requests.get(URL, timeout=10).text

    soup = BeautifulSoup(html, "html.parser")

    data = []

    # ⚠️ 实际网页结构可能变化，这里做通用解析示例
    rows = soup.find_all("div")

    for r in rows:

        text = r.get_text(" ", strip=True)

        nums = []

        for t in text.split():

            if t.isdigit():

                nums.append(int(t))

        if len(nums) >= 7:

            main = nums[:6]

            special = nums[6]

            data.append({

                "main": main,
                "special": special

            })

    with open("mark6_history.json","w") as f:

        json.dump(data[:200], f, indent=2)

    print("✅ history saved")


if __name__ == "__main__":
    fetch()