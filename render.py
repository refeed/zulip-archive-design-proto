import shutil

from jinja2 import Environment, FileSystemLoader

from fixtures import stream_list, topic_list, chat_list
from config import BASE_URL, INSTANCE_TITLE

environment = Environment(loader=FileSystemLoader("templates"), autoescape=True)
stream_list_template = environment.get_template("stream_list.html.jinja2")
topic_list_template = environment.get_template("topic_list.html.jinja2")
topic_chat_template = environment.get_template("topic_chat.html.jinja2")


with open("./rendered/index.html", mode="w+", encoding="utf-8") as f:
    f.write(
        stream_list_template.render(
            base_url=BASE_URL,
            page_title=INSTANCE_TITLE,
            title=INSTANCE_TITLE,
            last_updated_str="Archived on August 17th 2022 at 11.00 AM UTC",
            stream_list=stream_list,
        )
    )
with open("./rendered/stream.html", mode="w+", encoding="utf-8") as f:
    f.write(
        topic_list_template.render(
            base_url=BASE_URL,
            page_title=f"# lorem ipsum | {INSTANCE_TITLE}",
            title=INSTANCE_TITLE,
            last_updated_str="Archived on August 17th 2022 at 11.00 AM UTC",
            topic_list=topic_list,
            stream_name="lorem ipsum",
            stream_url=f"{BASE_URL}/stream.html",
        )
    )
with open("./rendered/topic.html", mode="w+", encoding="utf-8") as f:
    f.write(
        topic_chat_template.render(
            base_url=BASE_URL,
            page_title=f"Le fishe swimming in a bathtub - # lorem ipsum | {INSTANCE_TITLE}",
            title=INSTANCE_TITLE,
            last_updated_str="Archived on August 17th 2022 at 11.00 AM UTC",
            chat_list=chat_list,
            stream_name="lorem ipsum",
            stream_url=f"{BASE_URL}/stream.html",
            topic_name="Le fishe swimming in a bathtub",
            num_messages=3,
        )
    )


# Copy needed assets to /rendered
shutil.copytree("templates/assets", "rendered/assets", dirs_exist_ok=True)
