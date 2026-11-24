import json, os, subprocess, urllib.parse, urllib.request
Q = ["cheese platter","cheese board","brunch table","breakfast buffet","quiche","cheesecake","fruit tart","pastries","lasagna","fruit platter","focaccia","croissants","pasta cream sauce","mini desserts","shakshuka","salad bowl"]
os.makedirs("cand", exist_ok=True)
meta = []
UA = {"User-Agent": "catering-demo-fetch/1.0 (github actions)"}
for q in Q:
    url = "https://api.openverse.org/v1/images/?" + urllib.parse.urlencode({"q": q, "license_type": "commercial,modification", "page_size": 12, "size": "large", "mature": "false"})
    try:
        data = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40))
    except Exception as e:
        print("search fail", q, e); continue
    for i, r in enumerate(data.get("results", [])[:12]):
        fn = f"cand/{q.replace(' ','_')}_{i:02d}.jpg"
        try:
            req = urllib.request.Request(r["url"], headers=UA)
            raw = urllib.request.urlopen(req, timeout=40).read()
            open("tmp.bin","wb").write(raw)
            subprocess.run(["convert","tmp.bin[0]","-auto-orient","-resize","2000x2000>","-quality","82","-strip",fn], check=True, timeout=60)
            meta.append({"file": fn, "q": q, "title": r.get("title"), "creator": r.get("creator"), "license": r.get("license"), "license_version": r.get("license_version"), "source": r.get("foreign_landing_url"), "provider": r.get("provider"), "w": r.get("width"), "h": r.get("height")})
        except Exception as e:
            print("dl fail", fn, e)
json.dump(meta, open("cand/meta.json","w"), ensure_ascii=False, indent=1)
print(len(meta), "images")
