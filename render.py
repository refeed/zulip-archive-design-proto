import shutil

from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates"))
stream_list_template = environment.get_template("stream_list.html.jinja2")
topic_list_template = environment.get_template("topic_list.html.jinja2")
topic_chat_template = environment.get_template("topic_chat.html.jinja2")

# TODO: I think we need to use multiple template file instead of handling it like Blogger's case

with open("./rendered/index.html", mode="w+", encoding="utf-8") as f:
    f.write(stream_list_template.render())
with open("./rendered/stream.html", mode="w+", encoding="utf-8") as f:
    f.write(topic_list_template.render())
with open("./rendered/topic.html", mode="w+", encoding="utf-8") as f:
    f.write(topic_chat_template.render())


# Copy needed assets to /rendered
shutil.copyfile("pygments.css", "rendered/pygments.css")
