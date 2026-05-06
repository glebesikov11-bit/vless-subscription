import json
from datetime import datetime

SERVER_IP = "109.120.189.213"
SERVER_PORT = "58652"
PUBLIC_KEY = "VZq5atMvE_1AW0nXcn4opuxZdrSu3zy3kP7YTdGj6EQ"
SHORT_ID = "28"
SNI = "www.apple.com"

def main():
    try:
        with open("users.json", "r", encoding="utf-8") as f:
            users = json.load(f)
    except:
        users = []

    active_users = []
    vless_links = []
    today = datetime.today().date()

    for user in users:
        try:
            expire_date = datetime.strptime(user["expire_at"], "%Y-%m-%d").date()
            if expire_date >= today:
                active_users.append(user)
                link = f"vless://{user['id']}@{SERVER_IP}:{SERVER_PORT}?encryption=none&security=reality&sni={SNI}&fp=chrome&pbk={PUBLIC_KEY}&sid={SHORT_ID}#{user['name']}"
                vless_links.append(link)
        except:
            pass

    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(active_users, f, indent=2, ensure_ascii=False)

    with open("sub.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(vless_links))

    print(f"✅ Активных: {len(active_users)}")

if __name__ == "__main__":
    main()
