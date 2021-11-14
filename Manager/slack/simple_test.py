import os
from slack_sdk.rtm_v2 import RTMClient

rtm = RTMClient(token=os.environ["SLACK_BOT_TOKEN"])


@rtm.on("message")
def handle(client: RTMClient, event: dict):
    if 'Hello' in event['text']:
        channel_id = event['channel']
        thread_ts = event['ts']
        user = event['user']  # This is not username but user ID (the format is either U*** or W***)

        client.web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hi <@{user}>!",
            thread_ts=thread_ts
        )


rtm.start()
