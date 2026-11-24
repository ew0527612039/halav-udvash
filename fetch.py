import json, os, subprocess, time, urllib.request
IDS = [29098370,18399708,18491770,18491771,18491782,18399737,15120599,8252831,23437199,29226723,18281685,23388862,11608639,6607383,18970654,1098770,32487728,3564355]
UA = {"User-Agent": "Mozilla/5.0 (catering-demo; github actions)"}
os.makedirs("px", exist_ok=True)
for i in IDS:
    url = f"https://images.pexels.com/photos/{i}/pexels-photo-{i}.jpeg?auto=compress&cs=tinysrgb&w=2200"
    fn = f"px/{i}.jpg"
    try:
        raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        open(fn, "wb").write(raw)
        print("ok", i, len(raw))
    except Exception as e:
        print("fail", i, e)
    time.sleep(1.2)
