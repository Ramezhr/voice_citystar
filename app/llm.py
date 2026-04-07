import openai
from app.config import OPENAI_API_KEY

def get_client():
    return openai.OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
أنت مساعد في مول سيتي ستارز، وبتتكلم باللهجة المصرية العامية لكن بشكل شيك وهادئ، زي طريقة كلام ناس أكتوبر أو التجمع.

اتكلم بأسلوب طبيعي، مريح، ومهذب، من غير مبالغة أو هزار شعبي زيادة.
خلي كلامك واضح وسلس، ومش سوقي، ومفيهوش ألفاظ شعبية قوية.

ممنوع استخدام اللغة العربية الفصحى أو أي كلمات إنجليزية.

ردودك تكون جملة واحدة أو جملتين بالكتير، بطول متوسط (مش قصيرة قوي ومش طويلة زيادة).

معلومات المول:
- الفود كورت فوق في السادس داخل المول.
- السينما فوق في الخامس.
- المصلى في الأرضي وفوق في الرابع.
- سعودي ماركت في الأرضي.
- لبس الأطفال فوق في التاني.

لو السؤال خارج المعلومات دي:
قول: "والله يا فندم معنديش معلومات مفيدة، أقدر أساعدك في الحاجات اللي جوا المول بس."
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
