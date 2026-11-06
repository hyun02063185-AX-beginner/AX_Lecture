import re, pathlib, sys
cap=int(sys.argv[1]); ids=sys.argv[2:]
N=re.compile(r"(실제로|한 번은|예전에|작년에|저희 (회사|팀)|제가 (다니|있던|했던|예전|처음|만났)|어떤 (회사|대표|분|직원|고객)|대표님이|고객사|퇴사|날아|망|사고|실수|실패|포기|유출|야근|만\s?원|억|\d+\s?(시간|개월|명|배|%|프로|건|년))")
for vid in ids:
    L=[re.sub(r"^\[(\d+:\d+)\] ",r"\1 ",l) for l in pathlib.Path(f"txt/{vid}.txt").read_text(encoding="utf-8").split("\n")]
    sc=[len(N.findall(l)) for l in L]
    # window score
    W=[sum(sc[i:i+6]) for i in range(len(L))]
    picked=[];used=set()
    for i in sorted(range(len(L)),key=lambda i:-W[i]):
        if W[i]<2: break
        if any(abs(i-j)<6 for j in picked): continue
        picked.append(i)
        if sum(len(" ".join(L[j:j+6])) for j in picked)>cap: break
    out=[]
    for i in sorted(picked):
        seg=L[i:i+6]; out.append(seg[0][:5]+" "+" ".join(s[6:] for s in seg))
    print(f"## {vid}\n"+"\n".join(out)+"\n")
