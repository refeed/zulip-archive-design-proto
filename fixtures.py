from config import BASE_URL

stream_list = []
stream_list.append(
    dict(
        stream_name="lorem ipsum",
        url=f"{BASE_URL}/stream.html",
        num_topics=1,
        num_messages=2,
        last_date="August 13th 2022 at 10.00 PM",
        rendered_description="""
For discussions of the <a href="/api/rest" target="_blank" rel="noopener noreferrer" title="https://chat.zulip.org/api/rest">API</a>, <a href="/integrations" target="_blank" rel="noopener noreferrer" title="https://chat.zulip.org/integrations">integrations</a>, and <a href="/api/running-bots" target="_blank" rel="noopener noreferrer" title="https://chat.zulip.org/api/running-bots">bots</a> and&nbsp;in Zulip.
""",
    )
)
stream_list.append(
    dict(
        stream_name="swimming turtle",
        url="#",
        num_topics=1,
        num_messages=2,
        last_date="August 13th 2022 at 10.00 PM",
        rendered_description="""
For discussions of the <a href="/api/rest" target="_blank" rel="noopener noreferrer" title="https://chat.zulip.org/api/rest">API</a>, <a href="/integrations" target="_blank" rel="noopener noreferrer" title="https://chat.zulip.org/integrations">integrations</a>, and <a href="/api/running-bots" target="_blank" rel="noopener noreferrer" title="https://chat.zulip.org/api/running-bots">bots</a> and&nbsp;in Zulip.
""",
    )
)
stream_list.append(
    dict(
        stream_name="integration",
        url="#",
        num_topics=1,
        num_messages=2,
        last_date="August 13th 2022 at 10.00 PM",
        rendered_description="""
For discussions of the <a href="/api/rest" target="_blank" rel="noopener noreferrer" title="https://chat.zulip.org/api/rest">API</a>, <a href="/integrations" target="_blank" rel="noopener noreferrer" title="https://chat.zulip.org/integrations">integrations</a>, and <a href="/api/running-bots" target="_blank" rel="noopener noreferrer" title="https://chat.zulip.org/api/running-bots">bots</a> and&nbsp;in Zulip.
""",
    )
)

topic_list = []
topic_list.append(
    dict(
        topic_name="Le fishe swimming in a bathtub",
        url="#",
        num_messages=2,
        last_date="August 13th 2022 at 10.00 PM",
    )
)
topic_list.append(
    dict(
        topic_name="Swimming turtle",
        url="#",
        num_messages=32,
        last_date="August 13th 2022 at 10.00 PM",
    )
)
topic_list.append(
    dict(
        topic_name="Something lorem",
        url="#",
        num_messages=22,
        last_date="August 13th 2022 at 10.00 PM",
    )
)

chat_list = []
chat_list.append(
    dict(
        zulip_link="#",
        user_name="Rafid Aslam",
        date="August 17th at 20.22",
        msg_id=1,
        msg_content_html="""
<p>Say I write something like</p>
<div class="codehilite" data-code-language="Julia console">
<pre><span></span><code><span class="gp">julia&gt;</span><span class="w"></span><span class="k">ccall</span><span class="p">(</span><span class="ss">:printf</span><span class="p">,</span><span class="w"></span><span class="kt">Int</span><span class="p">,</span><span class="w"></span><span class="p">(</span><span class="kt">Cstring</span><span class="p">,),</span><span class="w"></span><span class="s">"hello there!</span><span class="se">\n</span><span class="s">"</span><span class="p">)</span><span class="w"></span>
<span class="go">hello there!</span>
<span class="go">13</span>
</code></pre>
</div>
<p>
i,e,. without explicitly specifying a path to a library… what determines the default set of paths Julia will search for the <code>printf</code>function?
</p>""",
    )
)
chat_list.append(
    dict(
        zulip_link="#",
        user_name="Rafid Aslam",
        date="August 17th at 20.22",
        msg_id=2,
        msg_content_html="""
<p>So here's my proposed approach and what to use in implementing the previous discussed mockup design in <a href="#narrow/stream/101-design/topic/zulip-archive.20design/near/1411111" title="https://chat.zulip.org/#narrow/stream/101-design/topic/zulip-archive.20design/near/1411111">https://chat.zulip.org/#narrow/stream/101-design/topic/zulip-archive.20design/near/1411111</a></p>
<ul>
<li>I highly recommend Jinja for the templating engine, as it is mature, used by many projects to handle HTML format and other formats too, and provides built-in HTML escaping</li>
</ul>
<p><strong>What to include</strong></p>
<ul>
<li><code>codehilite</code> CSS class from Zulip's <code>pygments.css</code> so that the code blocks appear with colors, just like in the main app</li>
<li>Some important and widely-used part of Zulip's  <code>rendered_markdown.css</code>, so that mentions, blockquotes, code tag, etc will appear similar just like in the main app</li>
</ul>
<p><strong>Approach</strong></p>
<ol>
<li>Implement the previously discussd mockup in plain HTMLs as a prototype, host it somewhere in the internet, ask for more feedback from the contributors on where to improve</li>
<li>Template-ize the prototype HTMLs as Jinja templates</li>
<li>Change the current zulip-archive code to use Jinja library to render HTMLs</li>
</ol>
<p>Step 3 can be done in parallel with 1 and 2 since waiting for feedback probably will take sometime.</p>
<p>Any thoughts <span class="user-mention" data-user-id="2328">@Rein Zustand</span> <span class="user-mention" data-user-id="7">@Tim Abbott</span> ?</p>
""",
    )
)
chat_list.append(
    dict(
        zulip_link="#",
        user_name="Rafid Aslam",
        date="August 17th at 20.22",
        msg_id=2,
        msg_content_html="""
<p><span class="user-mention silent" data-user-id="699">Anders Kaseorg</span> <a href="#narrow/stream/127-integrations/topic/zulip-archive/near/1401309" title="https://chat.zulip.org/#narrow/stream/127-integrations/topic/zulip-archive/near/1401309">said</a>:</p>
<blockquote>
<p>Reusing CSS files in different contexts is a recipe for disaster.</p>
</blockquote>
<p>This might be a silly question, but is the disaster like when we use it in zulip-archive then there's an update in zulip core's <code>rendered_markdown.css</code>, we have to update it in zulip-archive again? Or there's more that I'm not aware of?</p>
""",
    )
)
chat_list.append(
    dict(
        zulip_link="#",
        user_name="Rafid Aslam",
        date="August 17th at 20.22",
        msg_id=2,
        msg_content_html="""
<h1>Heading 1</h1>
<p>hello</p>
<h2>Heading 2</h2>
<p>hello</p>
<h3>Heading 3</h3>
<p>hello</p>
<h4>Heading 4</h4>
<p>hello</p>
<h5>Heading 5</h5>
<p>hello</p>
<h6>Heading 6</h6>
<p>hello</p>
""",
    )
)
