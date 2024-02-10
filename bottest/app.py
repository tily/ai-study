from datetime import datetime
import logging
import os
import sys
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.event("app_mention")
def app_mention(event, client, say, logger):
    logger.info(event)

    to = event["user"]
    text = f"<@{to}> Hello"

    if "thread_ts" in event:
        response = client.conversations_replies(
            channel=event["channel"],
            ts=event["thread_ts"],
        )
        for message in response["messages"]:
            datetime_str = datetime.fromtimestamp(int(float(message["ts"])))
            logger.info(f"{message['user']}: {message['text']} ({datetime_str})")

        say(text=text, thread_ts=event["thread_ts"])
    else:
        say(text=text, thread_ts=event["ts"])

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
