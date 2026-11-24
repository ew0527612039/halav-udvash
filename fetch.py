import json, os, subprocess, time, urllib.request
IDS = [725991,3872370,3872365,1640777,4198015,6605770,6605778,1279330,1437267,1438672,2097090,5949888,1527603,3763847,4079520,6287525]
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
for name,url in [("pix_greek","https://cdn.pixabay.com/photo/2017/03/25/10/21/salad-2173214_1280.jpg"),("pix_salad2","https://cdn.pixabay.com/photo/2015/05/31/13/59/salad-791891_1280.jpg")]:
    try:
        open(f"px/{name}.jpg","wb").write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()); print("ok",name)
    except Exception as e: print("fail",name,e)
