from openai import OpenAI

# 使用 API Key 鉴权
client = OpenAI(
    api_key="your api key",
    base_url="your api base url",
)

def chat_with_ernie(prompt_text, model="ernie-4.5-8k-preview", temperature=0.8):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": [{"type": "text", "text": prompt_text}]}],
        temperature=temperature
    )
    return response.choices[0].message.content
