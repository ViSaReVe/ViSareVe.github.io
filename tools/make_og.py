import numpy as np
from PIL import Image, ImageDraw, ImageFont

BG="#0e0e10"; TEXT="#f5f5f5"; MUTED="#9a9a9e"; ACCENT="#6ea8fe"; BORDER="#2a2a2e"

def font(cands, size):
    for path, idx in cands:
        try: return ImageFont.truetype(path, size, index=idx)
        except Exception: pass
    return ImageFont.load_default()

BOLD=[("/System/Library/Fonts/HelveticaNeue.ttc",1),("/System/Library/Fonts/Supplemental/Arial Bold.ttf",0)]
REG =[("/System/Library/Fonts/HelveticaNeue.ttc",0),("/System/Library/Fonts/Supplemental/Arial.ttf",0)]
MONO=[("/System/Library/Fonts/Menlo.ttc",1),("/System/Library/Fonts/Menlo.ttc",0),("/System/Library/Fonts/Supplemental/Courier New Bold.ttf",0)]

def tracked(d, xy, text, f, fill, track=0):
    x,y=xy
    for ch in text:
        d.text((x,y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + track
    return x

W,H=1200,630
img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)

# ── EMG-style waveform band (the same motif as the favicon) ──
rng=np.random.default_rng(7)
n=W
t=np.linspace(0,1,n)
env=np.zeros(n)
for c,w,a in [(0.22,0.045,0.45),(0.42,0.06,1.0),(0.63,0.05,0.7),(0.85,0.04,0.35)]:
    env += a*np.exp(-((t-c)**2)/(2*w**2))
sig=rng.standard_normal(n)
sig=np.convolve(sig,np.ones(5)/5,mode="same")
y=sig*env
y/= (np.abs(y).max() or 1)
cy, amp = 486, 78
pts=[(i, cy - y[i]*amp) for i in range(n)]

# faint full trace, brighter where the bursts are
for i in range(n-1):
    a = float(env[i]/env.max())
    shade = tuple(int(round(14 + (int(ACCENT[j:j+2],16)-14)*(0.14+0.72*a))) for j in (1,3,5))
    d.line([pts[i],pts[i+1]], fill=shade, width=2)

# baseline
d.line([(0,cy),(W,cy)], fill="#1a1a1e", width=1)

# ── text ──
f_name=font(BOLD,64); f_role=font(MONO,21); f_body=font(REG,27)
f_chip=font(REG,22); f_url=font(MONO,23)

d.text((72,86), "Vidya Sagar Reddy Venna", font=f_name, fill=TEXT)
tracked(d,(74,176),"ML & SIGNAL-PROCESSING ENGINEER",f_role,ACCENT,track=2.4)

d.text((72,228), "Biosignals · neural decoding · time-series ML", font=f_body, fill=MUTED)
d.text((72,268), "MS ECE (ML & Data Science) @ USC · May 2026", font=f_body, fill=MUTED)

# proof chips
x=72
for label in ["3 peer-reviewed papers","4 public sEMG datasets","88.3% ISI accuracy"]:
    w=d.textlength(label,font=f_chip)+34
    d.rounded_rectangle([x,330,x+w,376], radius=23, outline=BORDER, width=1)
    d.text((x+17,342), label, font=f_chip, fill="#c9c9cf")
    x+=w+14

d.text((72,566), "visareve.github.io", font=f_url, fill=TEXT)

img.save("assets/img/og-card.png", optimize=True)
print("og-card.png", img.size)

# ── apple-touch-icon: same mark as favicon.svg ──
S=180*4
ic=Image.new("RGB",(S,S),"#2563eb"); di=ImageDraw.Draw(ic)
m=Image.new("L",(S,S),0); ImageDraw.Draw(m).rounded_rectangle([0,0,S-1,S-1],radius=int(S*7/32),fill=255)
path=[(4,16),(9,16),(11.4,8.5),(14.5,23.5),(17.5,12.5),(19.9,16),(28,16)]
k=S/32
di.line([(px*k,py*k) for px,py in path], fill="#ffffff", width=int(2.6*k), joint="curve")
out=Image.new("RGB",(S,S),BG); out.paste(ic,(0,0),m)
out.resize((180,180), Image.LANCZOS).save("assets/img/apple-touch-icon.png", optimize=True)
print("apple-touch-icon.png ok")
