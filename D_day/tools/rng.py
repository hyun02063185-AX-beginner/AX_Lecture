import sys, pathlib, re
# usage: rng.py vid:mm:ss-mm:ss ...
def sec(x): m,s=x.split(":"); return int(m)*60+int(s)
for arg in sys.argv[1:]:
    vid, r = arg.split("@") if "@" in arg else (arg, "00:00-999:00")
    a,b = [sec(x) for x in r.split("-")]
    lines = pathlib.Path(f"txt/{vid}.txt").read_text(encoding="utf-8").split("\n")
    sel=[]
    for i,l in enumerate(lines):
        m=re.match(r"\[(\d+):(\d+)\] (.*)", l)
        if not m: continue
        t=int(m.group(1))*60+int(m.group(2))
        if a<=t<=b: sel.append((t,m.group(3)))
    # compact: timestamp every ~30s
    out=[]; lastts=-99
    for t,x in sel:
        if t-lastts>=30: out.append(f"\n[{t//60:02d}:{t%60:02d}] "); lastts=t
        out.append(x+" ")
    print(f"##### {vid} {r}\n{''.join(out).strip()}\n")
