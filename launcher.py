import subprocess, sys, json, os, shutil

CFG = "config.json"

def banner():
    print("\033[92m")
    print("████████╗██╗   ██╗██╗  ██╗██╗███╗   ██╗")
    print("╚══██╔══╝██║   ██║██║  ██║██║████╗  ██║")
    print("   ██║   ██║   ██║███████║██║██╔██╗ ██║")
    print("   ██║   ██║   ██║██╔══██║██║██║╚██╗██║")
    print("   ██║    ╚██████╔╝██║  ██║██║██║ ╚████║")
    print("   ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝")
    print("\033[0mSecure Player Launcher\n")

def load():
    with open(CFG) as f:
        return json.load(f)

def save(c):
    with open(CFG,"w") as f:
        json.dump(c,f,indent=2)

def start():
    subprocess.Popen([sys.executable,"app.py"])
    if shutil.which("cloudflared"):
        print("[*] Cloudflare Tunnel starting...")
        subprocess.Popen(
            ["cloudflared","tunnel","--url","http://127.0.0.1:5000"],
            stdout=sys.stdout,
            stderr=sys.stdout
        )
    else:
        print("[!] cloudflared not found")

banner()
while True:
    print("""
1) Start YouTube server
2) Start reCAPTCHA server
3) Change YouTube video link
4) Change storage path
5) Exit
""")
    c = load()
    o = input("Select: ").strip()
    if o=="1":
        c["recaptcha"]=False; save(c); start()
    elif o=="2":
        c["recaptcha"]=True; save(c); start()
    elif o=="3":
        c["video_url"]=input("New YouTube URL: "); save(c)
    elif o=="4":
        c["photo_dir"]=input("New storage path: "); save(c)
    elif o=="5":
        break
