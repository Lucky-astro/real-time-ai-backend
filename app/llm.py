import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found in environment")

client = AsyncOpenAI(api_key=api_key)

async def stream_llm_response(messages, websocket):
    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            stream=True
        )

        async for chunk in response:
            if chunk.choices and chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                await websocket.send_text(token)

    except Exception as e:
        print("🔥 OPENAI ERROR:", repr(e))
        await websocket.send_text("\n[AI ERROR]\n")
