import os
import shutil

from jinja2 import Environment, FileSystemLoader

BASE_URL = os.getenv("BASE_URL", "")
INSTANCE_TITLE = "Lorem Ipsum Community Archive"

environment = Environment(loader=FileSystemLoader("templates"))
stream_list_template = environment.get_template("stream_list.html.jinja2")
topic_list_template = environment.get_template("topic_list.html.jinja2")
topic_chat_template = environment.get_template("topic_chat.html.jinja2")


with open("./rendered/index.html", mode="w+", encoding="utf-8") as f:
    f.write(
        stream_list_template.render(
            base_url=BASE_URL, page_title=INSTANCE_TITLE, title=INSTANCE_TITLE
        )
    )
with open("./rendered/stream.html", mode="w+", encoding="utf-8") as f:
    f.write(
        topic_list_template.render(
            base_url=BASE_URL,
            page_title=f"# lorem ipsum | {INSTANCE_TITLE}",
            title=INSTANCE_TITLE,
        )
    )
with open("./rendered/topic.html", mode="w+", encoding="utf-8") as f:
    f.write(
        topic_chat_template.render(
            base_url=BASE_URL,
            page_title=f"Le fishe swimming in a bathtub - # lorem ipsum | {INSTANCE_TITLE}",
            title=INSTANCE_TITLE,
        )
    )


# Copy needed assets to /rendered
shutil.copytree("templates/assets", "rendered/assets", dirs_exist_ok=True)
