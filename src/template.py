import os
from core import load_json, here, web_name

data = load_json("tarot-img_onl")["tarot_interpretations"]


def make_html_from_card(card):

    content = f"""
        <p><strong>Keywords:</strong></br>{", ".join(card["keywords"])}</p>
        <p><strong>Meanings:</strong></p>
        <p><u>Normal:</u></br> - {"</br> - ".join(card["meanings"]["light"])}</p>
        <p><u>Reversed:</u></br> - {"</br> - ".join(card["meanings"]["shadow"])}</p>
        <p><strong>Tellings:</strong></p>
        <p> - {"</br> - ".join(card["fortune_telling"])}</p>
    """
    content3 = f"""
        <strong>Keywords:</strong></br>{", ".join(card["keywords"])}</br>
        <strong>Meanings:</strong></br>
        <u>Normal:</u></br> - {"</br> - ".join(card["meanings"]["light"])}</br>
        <u>Reversed:</u></br> - {"</br> - ".join(card["meanings"]["shadow"])}</br>
        <strong>Tellings:</strong></br>
         - {"</br> - ".join(card["fortune_telling"])}</br>
    """

    template = f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Tarot Database:</title>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1">  
            <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
            <link rel="stylesheet" href="../style.css">
        </head>
        <body>
            <div class="w3-container">
                <h1 class="w3-center"><strong>Tarot Database</strong></h1>
                <p id="credit" align="center">
                    <i>Tarot data from</br>
                    Mark McElroy's <code>"Guide to Tarot Meanings"</code></i></br>
                </p>
            </div>
            <div class="w3-container box-2">
                <div class="w3-row w3-center w3-display-center">
                    <div class="w3-half" style="max-height: 70%">
                        <div class="w3-container w3-center">
                            <img id="tcard" src="{card["img"]}">
                        </div>
                    </div>
                    <div class="w3-half">
                        <div class="w3-container text_box">
                            <p id="main_text" align="left"><strong>Card: {card["name"]}</strong></p>
                            <p id="sup_text" align="left">{content3}</p>
                        </div>
                    </div>
                </div>
            </div>
        </body>
    </html>
    """
    return template


# def make_html(card):
#     html_content = make_html_from_card(card)
#     with open(f"{here}/{web_name(card['name'])}/index.html","w") as html_file:
#         html_file.writelines(html_content)

def make_html(card):
    html_content = make_html_from_card(card)
    if not os.path.exists(f"{here}/{web_name(card['name'])}/"):
        os.makedirs(f"{here}/{web_name(card['name'])}/")
    with open(f"{here}/{web_name(card['name'])}/index.html","w") as html_file:
        html_file.writelines(html_content)


def get_name(data):
    temp = []
    for x in data:
        temp.append(web_name(x["name"]))
    return temp


# def get_link(data):
#     for x in data:
#         text = f'<a href="/data/{web_name(x["name"])}.html">{x["name"]}</a></br>'
#         print(text)


def get_link(data):
    for x in data:
        text = f'<a href="/data/{web_name(x["name"])}/index.html">{x["name"]}</a></br>'
        print(text)


# for x in data: make_html(x)

# get_link(data)
