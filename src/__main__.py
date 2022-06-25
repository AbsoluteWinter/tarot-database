import subprocess

from core import load_json, save_json, here

# from rich import print

subprocess.call(f"{here}/script.py", shell=True)
subprocess.call(f"{here}/img.py", shell=True)

tarot = load_json("tarot-neo")
pics = load_json("imgs")
img_link = load_json("imgs1")


for x in tarot["tarot_interpretations"]:
    x["img64"] = pics[x["img"]]
save_json(tarot, "tarot-img64")
