import json, os, subprocess, time, urllib.request
IDS = [1741284,2290741,34621131,4577646,248413,1439328,6152263,7965947,27858799,3850394,6207315,88917,1485806,1448721,903400,5091144]
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
