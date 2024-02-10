import logging
import os
import re
import sys
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.event("app_mention")
def app_mention(event, say, logger):
    logger.info(event)

    to = event["user"]
    text = f"<@{to}> Hello"

    if "thread_ts" in event:
        say(text=text, thread_ts=event["thread_ts"])
    else:
        say(text=text, thread_ts=event["ts"])

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
