#!/usr/bin/env python3

from markdown import markdown
from datetime import datetime
import re
import argparse


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--id", help="post ID", required=True)
    parser.add_argument("-M", "--markdown", help="Markdown input file", required=True)
    parser.add_argument("-H", "--html", help="HTML output file", required=True)
    parser.add_argument("-R", "--rss", help="RSS output file", required=True)

    return parser.parse_args()


def render_HTML(date, html, file):
    with open(file, "r") as f:
        html = f.read().replace(
            """<div id="main_info">""", f"""<div id="main_info">\n{html + date}""",
        )

    with open(file, "w") as f:
        f.write(html)


def render_XML(date, title, body, file):
    with open(file, "r") as f:
        xml = re.sub(
            r"<lastBuildDate>.*</", f"<lastBuildDate>{date}</", f.read()
        ).replace(
            """</lastBuildDate>""",
            f"""</lastBuildDate>
<item>
<title>{title}</title>
<description><![CDATA[
{body}
]]></description>
<pubDate>{date}</pubDate>
</item>""",
        )

    with open(file, "w") as f:
        f.write(xml)


def main():
    args = arguments()

    with open(args.markdown, "r") as f:
        MARKDOWN_FILE = f.read()

    date = datetime.now()
    html_date = f"""<div class="date">{date.strftime("%Y-%m-%d %H:%M")}</div>"""
    xml_date = date.strftime("%a, %d %b %Y %H:%M:%S +0200")

    html = markdown(MARKDOWN_FILE, output_format="html5")
    title = html.split("\n")[0].replace("<h1>", "").replace("</h1>", "")
    html = html.replace(
        "<h1>", f"""<a href="#{args.id}"><h3><p class="wt">#{args.id}</p> """
    ).replace("</h1>", "</h3></a>")
    html = f"""<div id="{id}" class="project">\n{html}</div>"""
    body = html.splitlines()
    del body[0:2]
    body = " ".join(body).replace("</div>", "")

    render_HTML(html_date, html, args.html)
    render_XML(xml_date, title, body, args.rss)


if __name__ == "__main__":
    main()
