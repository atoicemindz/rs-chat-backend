import os
import openai
import google.generativeai as genai

# Ambil API key dari .env
openai.api_key = os.getenv("OPENAI_API_KEY")

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def ask_chatgpt(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Kamu adalah asisten rumah sakit yang membantu membaca laporan."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        reply = response.choices[0].message.content
        return reply
    except Exception as e:
        return f"Terjadi error saat menghubungi AI: {e}"


def ask_gemini(user_message):
    try:
        response = model.generate_content(user_message)
        return {"response": response.text}
    except Exception as e:
        return {"response": f"Terjadi error saat menghubungi Gemini: {str(e)}"}