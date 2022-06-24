import base64
import glob

from core import save_json, here


# GET LIST OF IMAGES
img_list = []
for filename in glob.glob(f"{here}/../images/*.jpg"):
    img_list.append(filename[len(filename)-7:])

# MAKE BASE64 DATA
imgs = {}
for x in img_list:
    with open(f"{here}/../images/{x}", "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
    imgs[x] = "data:image/jpeg;charset=utf-8;base64, " + b64_string.decode("utf-8")

# SAVE
save_json(imgs, "imgs")