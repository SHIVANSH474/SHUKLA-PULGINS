<h1 align="center">
  <b>𝑺𝑯𝑰𝑽-𝑶𝑷 🇮🇳</b>
</h1>

<p align="center">
  <img src="https://te.legra.ph/file/fd0c3c2201447746fd1d0.jpg" alt="The-HellBot">
</p>

<h6 align="center">
  <b>⚡ 𝑵𝑶𝑻𝑯𝑰𝑵𝑮 𝑺𝑷𝑬𝑪𝑨𝑰𝑳⚡</b>
</h6>

<h3 align="center">
  <b>A Smooth & Fast File for vc tool.</b>
</h3>

-----

<h1 align="center">
  <b>Follow this format to make your own vc tool</b>
</h1>

```python3
"""
A sample code to display hello without taking input.
"""
# this is a mandatory import
from . import *

# assigning command
@hell_cmd(pattern="hii$")
async def hi(event):
    # command body
    await eor(event, "Hello!")


# to display in help menu
CmdHelp("hii").add_command(
  "hii", None, "Says Hello!"
).add()
```
----
```python3
"""
A sample code to display hello with input.
"""
# this is a mandatory import
from . import *

# assigning command
@hell_cmd(pattern="hii(?:\s|$)([\s\S]*)")
async def hi(event):
    # command body
    _input = event.pattern_match.group(1)
    if _input:
        await eor(event, f"Hello! {_input}")
    else:
        await eor(event, "Hello!")


# to display in help menu
CmdHelp("hii").add_command(
    "hii", "<text>", "Display Hello with a input!"
).add()
```


### To get more functions read codes in repo.

------

## Disclaimer
- We won't be responsible for any kind of ban due to this bot.
- HellBot was made for fun purpose and to make group management easier.
- It's your concern if you spam and gets your account banned.
- Also, Forks won't be entertained.
- If you fork this repo and edit plugins, it's your concern for further updates.
- Forking Repo is fine. But if you edit something we will not provide any help.
- In short, Fork At Your Own Risk.


------
## Credits

- 💖 [Telethon](https://github.com/LonamiWebs/Telethon)
- 💖 [Pyrogram](https://github.com/Pyrogram/Pyrogram)
- 💖 Team Hellbot

------
