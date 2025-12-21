import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

# Create OpenAI async client
client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

async def stream_llm_response(messages, websocket):
    """
    Stream LLM response token-by-token over WebSocket
    """
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        stream=True,
    )

    async for chunk in response:
        if chunk.choices and chunk.choices[0].delta:
            content = chunk.choices[0].delta.content
            if content:
                await websocket.send_text(content)
