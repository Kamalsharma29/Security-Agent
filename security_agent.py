from datetime import datetime
from uuid import uuid4
import os
import requests
import json
from dotenv import load_dotenv
from uagents import Context, Protocol, Agent
from uagents_core.contrib.protocols.chat import (
    ChatAcknowledgement,
    ChatMessage,
    TextContent,
    chat_protocol_spec,
)

# Load API key from .env file
load_dotenv()
SAFE_BROWSING_API_KEY = os.getenv("SAFE_BROWSING_API_KEY")

agent = Agent(
    name="Security-Agent",
    seed="Security-Agent",
    port=8002,
    mailbox=True,
)

protocol = Protocol(spec=chat_protocol_spec)

@protocol.on_message(ChatMessage)
async def handle_message(ctx: Context, sender: str, msg: ChatMessage):
    # Acknowledge receipt
    await ctx.send(
        sender,
        ChatAcknowledgement(timestamp=datetime.now(), acknowledged_msg_id=msg.msg_id),
    )

    text = ""
    for item in msg.content:
        if isinstance(item, TextContent):
            text += item.text.strip()

    response = "Please provide a valid URL to check."

    try:
        if text.startswith("http"):
            api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={SAFE_BROWSING_API_KEY}"
            body = {
                "client": {"clientId": "security-agent", "clientVersion": "1.0"},
                "threatInfo": {
                    "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
                    "platformTypes": ["ANY_PLATFORM"],
                    "threatEntryTypes": ["URL"],
                    "threatEntries": [{"url": text}],
                },
            }

            r = requests.post(api_url, json=body)
            result = r.json()

            if "matches" in result:
                response = f"⚠️ ALERT: The URL `{text}` is flagged as **unsafe**!\nDetails: {json.dumps(result, indent=2)}"
            else:
                response = f"✅ The URL `{text}` seems **safe**."
        else:
            response = "Please send a valid URL starting with http/https."
    except Exception as e:
        ctx.logger.exception("Error checking URL")
        response = f"Error processing security check: {str(e)}"

    await ctx.send(sender, ChatMessage(
        timestamp=datetime.utcnow(),
        msg_id=uuid4(),
        content=[TextContent(type="text", text=response)],
    ))

@protocol.on_message(ChatAcknowledgement)
async def handle_ack(ctx: Context, sender: str, msg: ChatAcknowledgement):
    pass

agent.include(protocol, publish_manifest=True)

if __name__ == "__main__":
    agent.run()
