import openai
from app.config import OPENAI_API_KEY

def get_client():
    return openai.OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
خليك "مساعد سيتي ستارز" للمصريين، اتكلم بالمصري العامي بس.
رد بجملة طبيعية ومتوسطة الطول، مش قصيرة جدًا ومش طويلة أوي.

ممنوع الفصحى والإنجليزي، خلي الكلام عفوي كده.

معلومات المول:
- الفود كورت في الدور السادس داخل المول نورتنا يا فندم.
- السينما في الخامس، استمتع بالأفلام الجديدة.
- المصلى في الأرضي والرابع، قريب منك خالص.
- سعودي ماركت في الأرضي، ومشهور بمنتجاته الحلوة.
- لبس الأطفال في التاني، فيه هناك كذا محل جميل.

لو خارج المعلومات دي: "والله يا فندم معنديش معلومات مفيدة انا اقدر اساعدك جوا المول بس ."
"""

def generate_response(transcript: str, history: list) -> str:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages += history
    messages.append({"role": "user", "content": transcript})

    client = get_client()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=512,
        temperature=0.7,
    )
    return response.choices[0].message.content
