import json,os,sys,urllib.request as REQ,urllib.error as E
U=os.environ.get("MAKEFUN_ENV_URL")
def post(p,b):
 try:
  q=REQ.Request(U+p,data=json.dumps(b).encode(),headers={'Content-Type':'application/json'})
  with REQ.urlopen(q) as f:return json.loads(f.read())
 except E.HTTPError as e:sys.exit()
P,N,B,R,Q,K=1,2,3,4,5,6
V=[0,100,320,330,500,900,0]
# PSTs minified
T1=[0]*8+[5,10,10,-20,-20,10,10,5,5,-5,-10,0,0,-10,-5,5,0,0,0,20,20,0,0,0,5,5,10,25,25,10,5,5,10,10,20,30,30,20,10,10,50,50,50,50,50,50,50,50]+[0]*8
T2=[-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,5,5,0,-20,-40,-30,5,10,15,15,10,5,-30,-30,0,15,20,20,15,0,-30,-30,5,15,20,20,15,5,-30,-30,0,10,15,15,10,0,-30,-40,-20,0,0,0,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50]
T3=[-20,-10,-10,-10,-10,-10,-10,-20,-10,5,0,0,0,0,5,-10,-10,10,10,10,10,10,10,-10,-10,0,10,10,10,10,0,-10,-10,5,5,10,10,5,5,-10,-10,0,5,10,10,5,0,-10,-10,0,0,0,0,0,0,-10,-20,-10,-10,-10,-10,-10,-10,-20]
T4=[0,0,0,5,5,0,0,0,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,5,10,10,10,10,10,10,5,0,0,0,0,0,0,0,0]
T5=[-20,-10,-10,-5,-5,-10,-10,-20,-10,0,5,0,0,0,0,-10,-10,5,5,5,5,5,0,-10,0,0,5,5,5,5,0,-5,-5,0,5,5,5,5,0,-5,-10,0,5,5,5,5,0,-10,-10,0,0,0,0,0,0,-10,-20,-10,-10,-5,-5,-10,-10,-20]
T6=[20,30,10,0,0,10,30,20,20,20,0,0,0,0,20,20,-10,-20,-20,-20,-20,-20,-20,-10,-20,-30,-30,-40,-40,-30,-30,-20,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30]
T={1:T1,2:T2,3:T3,4:T4,5:T5,6:T6}
ZK=[];X=12345
for _ in range(781):X=(X*1103515245+12345)&0x7fffffff;ZK.append(X)
BUDGET=12000;NS=0;ABORT=0;TT={};HY={};KL=[[None]*2 for _ in range(64)]
def GH(b,s,c,e):
 h=0 if s>0 else ZK[768]
 for i,p in enumerate(b):
  if p:h^=ZK[i*12+(p+6 if p<0 else p-1)]
 for i in range(4):
  if c&(1<<i):h^=ZK[769+i]
 if e!=-1:h^=ZK[773+e%8]
 return h
def M(b,s,c,e,m):
 f,t,p=m;nb=b[:];ns=-s;nc=c;ne=-1;pc=b[f];nb[t]=pc;nb[f]=0
 if p:nb[t]=s*p
 if abs(pc)==1:
  if t==e:nb[t-s*8]=0
  if abs(t-f)==16:ne=(f+t)//2
 if abs(pc)==6:
  if t-f==2:nb[f+1],nb[f+3]=b[f+3],0
  if t-f==-2:nb[f-1],nb[f-4]=b[f-4],0
  nc&=(12 if s==1 else 3)
 for i,x in [(0,2),(7,1),(56,8),(63,4)]:
  if f==i or t==i:nc&=~x
 return nb,ns,nc,ne
def A(b,sq,s):
 tr,tc=sq//8,sq%8
 for i in range(64):
  p=b[i]
  if p*s>0:
   ap=abs(p);r,c=i//8,i%8;dr,dc=tr-r,tc-c
   if ap==1:
    if (s==1 and dr==1 and abs(dc)==1) or (s==-1 and dr==-1 and abs(dc)==1):return 1
   elif ap==2:
    if (abs(dr),abs(dc)) in [(1,2),(2,1)]:return 1
   elif ap==6:
    if abs(dr)<=1 and abs(dc)<=1:return 1
   elif (dr==0 or dc==0) and ap in [4,5]:
    sr,sc=(dr//abs(dr) if dr else 0),(dc//abs(dc) if dc else 0);cr,cc=r+sr,c+sc;ok=1
    while cr!=tr or cc!=tc:
     if b[cr*8+cc]:ok=0;break
     cr+=sr;cc+=sc
    if ok:return 1
   elif abs(dr)==abs(dc) and ap in [3,5]:
    sr,sc=dr//abs(dr),dc//abs(dc);cr,cc=r+sr,c+sc;ok=1
    while cr!=tr or cc!=tc:
     if b[cr*8+cc]:ok=0;break
     cr+=sr;cc+=sc
    if ok:return 1
 return 0
def G(b,s,c,e):
 res=[]
 for f in range(64):
  p=b[f]
  if p*s>0:
   ap=abs(p);r,c_=f//8,f%8
   if ap==1:
    st=8*s
    if 0<=f+st<64 and b[f+st]==0:
     if (s==1 and r==6) or (s==-1 and r==1):
      for pr in [5,4,3,2]:res.append((f,f+st,pr))
     else:
      res.append((f,f+st,0))
      if ((s==1 and r==1) or (s==-1 and r==6)) and 0<=f+2*st<64 and b[f+2*st]==0:res.append((f,f+2*st,0))
    for dc in [-1,1]:
     t=f+st+dc
     if 0<=t<64 and abs(t%8-c_)==1 and (b[t]*s<0 or t==e):
      if (s==1 and r==6) or (s==-1 and r==1):
       for pr in [5,4,3,2]:res.append((f,t,pr))
      else:res.append((f,t,0))
   elif ap==2:
    for dr,dc in [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]:
     tr,tc=r+dr,c_+dc
     if 0<=tr<8 and 0<=tc<8 and b[tr*8+tc]*s<=0:res.append((f,tr*8+tc,0))
   elif ap==6:
    for dr in [-1,0,1]:
     for dc in [-1,0,1]:
      if (dr or dc) and 0<=r+dr<8 and 0<=c_+dc<8 and b[(r+dr)*8+c_+dc]*s<=0:res.append((f,(r+dr)*8+c_+dc,0))
    if s==1:
     if (c&1) and not b[5] and not b[6] and not A(b,4,-1) and not A(b,5,-1) and not A(b,6,-1):res.append((4,6,0))
     if (c&2) and not b[1] and not b[2] and not b[3] and not A(b,4,-1) and not A(b,3,-1) and not A(b,2,-1):res.append((4,2,0))
    else:
     if (c&4) and not b[61] and not b[62] and not A(b,60,1) and not A(b,61,1) and not A(b,62,1):res.append((60,62,0))
     if (c&8) and not b[57] and not b[58] and not b[59] and not A(b,60,1) and not A(b,59,1) and not A(b,58,1):res.append((60,58,0))
   else:
    ds=[]
    if ap in [4,5]:ds+=[(0,1),(0,-1),(1,0),(-1,0)]
    if ap in [3,5]:ds+=[(1,1),(1,-1),(-1,1),(-1,-1)]
    for dr,dc in ds:
     tr,tc=r+dr,c_+dc
     while 0<=tr<8 and 0<=tc<8:
      t=tr*8+tc
      if not b[t]:res.append((f,t,0))
      elif b[t]*s<0:res.append((f,t,0));break
      else:break
      tr+=dr;tc+=dc
 return res
def E(b,s):
 sc=0;wc=bc=0
 for i,p in enumerate(b):
  if p:
   ap=abs(p);v=V[ap]+T[ap][i if p>0 else i^56]
   if p>0:
    sc+=v
    if ap==3:wc+=1
    if ap==1:sc+=[0,10,20,30,50,80,120][i//8]
   else:
    sc-=v
    if ap==3:bc+=1
    if ap==1:sc-=[0,10,20,30,50,80,120][7-i//8]
 if wc>=2:sc+=30
 if bc>=2:sc-=30
 return sc*s
def Q(b,s,c,e,a,bt):
 global NS,ABORT
 if NS>=BUDGET:ABORT=1;return 0
 NS+=1;king=next(i for i,p in enumerate(b) if p==s*6);check=A(b,king,-s)
 legal=[]
 for m in G(b,s,c,e):
  nb,ns,nc,ne=M(b,s,c,e,m)
  if not A(nb,[i for i,p in enumerate(nb) if p==s*6][0],-s):legal.append(m)
 if not legal:return -999900 if check else 0
 if not check:
  sp=E(b,s)
  if sp>=bt:return sp
  if a<sp:a=sp
 ms=legal if check else [m for m in legal if b[m[1]] or m[2]]
 ms.sort(key=lambda m:V[abs(b[m[1]])]*10-V[m[2] or abs(b[m[0]])],reverse=True)
 for m in ms:
  nb,ns,nc,ne=M(b,s,c,e,m)
  sc=-Q(nb,ns,nc,ne,-bt,-a)
  if ABORT:return 0
  if sc>=bt:return sc
  if sc>a:a=sc
 return a
def S(b,s,c,e,d,a,bt,p,hh):
 global NS,ABORT
 if NS>=BUDGET:ABORT=1;return 0
 NS+=1;al,be=a,bt
 h=GH(b,s,c,e)
 if h in hh:return 0
 if h in TT:
  td,ts,tf,tm=TT[h]
  if td>=d:
   if tf==0:return ts
   if tf==1 and ts<=a:return ts
   if tf==2 and ts>=bt:return ts
 if d<=0:return Q(b,s,c,e,a,bt)
 ms=G(b,s,c,e);tm=TT[h][3] if h in TT else None
 ms.sort(key=lambda m:(1e9 if m==tm else V[abs(b[m[1]])]*10-V[m[2] or abs(b[m[0]])]+1e5 if b[m[1]] else 5e4 if m in KL[p] else HY.get((m[0],m[1]),0)),reverse=True)
 bs,mc,bm=-1e9,0,None
 for m in ms:
  nb,ns,nc,ne=M(b,s,c,e,m)
  if A(nb,[i for i,p in enumerate(nb) if p==s*6][0],-s):continue
  mc+=1;sc=-S(nb,ns,nc,ne,d-1,-bt,-a,p+1,hh+[h])
  if ABORT:return 0
  if NS>=6000 and d>1: return a
  if sc>bs:bs,bm=sc,m
  if sc>a:a=sc
  if a>=bt:
   if not b[m[1]]:HY[(m[0],m[1])]=HY.get((m[0],m[1]),0)+d*d;KL[p][1],KL[p][0]=KL[p][0],m
   break
 if mc==0:return -999900+p if A(b,[i for i,p in enumerate(b) if p==s*6][0],-s) else 0
 TT[h]=(d,bs,0 if bs>al and bs<be else (2 if bs>=be else 1),bm)
 return bs
def best(g):
 global NS,ABORT,TT;f=g["start_fen"].split();b=[0]*64;r,c=7,0
 for ch in f[0]:
  if ch=='/':r-=1;c=0
  elif ch.isdigit():c+=int(ch)
  else:p="PNBRQKpnbrqk".find(ch);b[r*8+c]=(p+1 if p<6 else -(p-5));c+=1
 s,ct=1 if f[1]=='w' else -1,0
 for ch,v in [('K',1),('Q',2),('k',4),('q',8)]:
  if ch in f[2]:ct|=v
 e=-1 if f[3]=='-' else (ord(f[3][0])-97)+(int(f[3][1])-1)*8
 hh=[]
 for u in g["moves"]:
  hh.append(GH(b,s,ct,e));fm,to,pr=ord(u[0])-97+(int(u[1])-1)*8,ord(u[2])-97+(int(u[3])-1)*8,0
  if len(u)==5:pr={"n":2,"b":3,"r":4,"q":5}[u[4]]
  b,s,ct,e=M(b,s,ct,e,(fm,to,pr))
 NS,bm=0,None
 for d in range(1,20):
  ABORT=0;root=GH(b,s,ct,e)
  S(b,s,ct,e,d,-1e9,1e9,0,hh)
  if ABORT:break
  if root in TT:bm=TT[root][3]
 if not bm:bm=G(b,s,ct,e)[0]
 f,t,p=bm;u=chr(f%8+97)+str(f//8+1)+chr(t%8+97)+str(t//8+1)
 if p:u+=" pnbrq"[p]
 return u
while 1:
 g=post("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":g=post("/move",{"game":g["game"],"move":best(g)})
 print(f"Outcome: {g.get('outcome')}",file=sys.stderr)
print("done",file=sys.stderr)
