import re, pathlib
src = pathlib.Path("subs"); dst = pathlib.Path("txt"); dst.mkdir(exist_ok=True)
for f in sorted(src.glob("*.ko.vtt")):
    vid = f.name.split(".")[0]; out=[]; recent=[]
    for b in f.read_text(encoding="utf-8").split("\n\n"):
        m = re.search(r"(\d\d):(\d\d):(\d\d)\.\d+ -->", b)
        if not m: continue
        h,mi,s = map(int,m.groups()); t=h*3600+mi*60+s
        for l in b.split("\n")[1:]:
            x = re.sub(r"<[^>]+>","",l).strip()
            if not x or "-->" in x or x in recent: continue
            recent = (recent+[x])[-6:]
            out.append(f"[{t//60:02d}:{t%60:02d}] {x}")
    (dst/f"{vid}.txt").write_text("\n".join(out),encoding="utf-8")
