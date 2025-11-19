import requests, time

PUMP_FUN_API = "https://pump.fun/api/token/"

def watch_new_tokens():
    print("Снайпер Pump.fun запущен...")
    seen = set()
    while True:
        r = requests.get("https://pump.fun/api/tokens?limit=20&offset=0")
        for t in r.json()["tokens"]:
            addr = t["mint"]
            if addr not in seen and t["created_timestamp"] > time.time() - 60:
                seen.add(addr)
                print(f"НОВЫЙ ТОКЕН!\n"
                      f"Имя: {t['symbol']} | {t['name']}\n"
                      f"CA: {addr}\n"
                      f"Ссылка: https://pump.fun/{addr}\n"
                      f"Создан: {time.strftime('%H:%M:%S', time.localtime(t['created_timestamp']))}\n"
                      f"{'-'*40}")
        time.sleep(5)

if __name__ == "__main__":
    watch_new_tokens()
