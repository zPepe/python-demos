import json
from datetime import datetime

import jinja2
import pdfkit

with open("nmap.json") as target:
    report = json.load(target)

print(report)
templateLoader = jinja2.FileSystemLoader(searchpath="./")

templateEnv = jinja2.Environment(loader=templateLoader)

TEMPLATE_FILE = "template.html"

template = templateEnv.get_template(TEMPLATE_FILE)


def get_css_as_string(name):
    with open(name, "r") as f:
        return f.read()


outputText = template.render(
    data=report, date=datetime.now().strftime("%Y-%m-%d %H:%M"), css_string=get_css_as_string("static/style.css"))

with open("index.html", "w+") as target:
    target.write(outputText)


# Conversion of html to pdf
pdfkit.from_file('index.html', 'test.pdf')
