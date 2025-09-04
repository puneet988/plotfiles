# pip install fonttools
from fontTools.ttLib import TTCollection
from pathlib import Path
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

ttc_path = Path("/Users/puneetsharma/puneet/fontfolder/HelveticaNeue.ttc")
out_dir = ttc_path.with_suffix("")  # e.g., .../HelveticaNeue
out_dir.mkdir(exist_ok=True)

ttc = TTCollection(str(ttc_path))
saved = []
for i, tt in enumerate(ttc.fonts):
    name = tt["name"]
    fam = (name.getName(1,3,1,1033) or name.getName(1,1,0,0)).toUnicode()
    sub = (name.getName(2,3,1,1033) or name.getName(2,1,0,0)).toUnicode()
    psn = (name.getName(6,3,1,1033) or name.getName(6,1,0,0)).toUnicode()
    ext = ".otf" if tt.sfntVersion == "OTTO" else ".ttf"
    out = out_dir / f"{psn or (fam+sub).replace(' ','')}{ext}"
    tt.save(out)
    print(i, fam, sub, "->", out)
    saved.append(out)

# Pick the file you want (say index 2 printed above)
chosen = str(saved[12])
prop = fm.FontProperties(fname=chosen)
plt.title("Specific face", fontproperties=prop)
plt.show()
