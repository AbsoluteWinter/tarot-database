"""
Make new tarot.json file (include images)
"""

from core import load_json, save_json

tarot = load_json("tarot")
tarot_card = load_json("tarot-images")
    
# Name cleaning
for i in range(len(tarot["tarot_interpretations"])):
    tarot["tarot_interpretations"][i]["name"] = tarot["tarot_interpretations"][i]["name"].title()
    tarot_card["cards"][i]["name"] = tarot_card["cards"][i]["name"].title()
    
    if tarot["tarot_interpretations"][i]["name"].endswith(("Priestess", "Hierophant", "Wheel", "Coins")):
        tarot["tarot_interpretations"][i]["name"] = tarot_card["cards"][i]["name"]
    # if (tarot["tarot_interpretations"][i]["name"] != tarot_card["cards"][i]["name"]):
    #     print(tarot["tarot_interpretations"][i]["name"], "---", tarot_card["cards"][i]["name"])

# Link image
for i in range(len(tarot["tarot_interpretations"])):
    for j in range(len(tarot_card["cards"])):
        if tarot["tarot_interpretations"][i]["name"] == tarot_card["cards"][j]["name"]:
            tarot["tarot_interpretations"][i]["img"] = tarot_card["cards"][j]["img"]
            break


save_json(tarot, "tarot-neo")


