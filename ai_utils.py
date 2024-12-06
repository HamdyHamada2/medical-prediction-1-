# import openai
# from django.conf import settings
#
# openai.api_key = settings.OPENAI_API_KEY
#
#
# def generate_diagnosis(symptoms):
#     try:
#         response = openai.ChatCompletion.create (
#             model="gpt-4",
#             messages=[
#                 {"role": "system", "content": "You are a medical assistant."},
#                 {"role": "user", "content": f"What is the diagnosis for these symptoms: {symptoms}?"}
#             ]
#         )
#         return response.choices[0].message["content"]
#     except Exception as e:
#         return f"Error: {e}"
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY


def generate_diagnosis(symptoms):
    try:
        # استخدم نموذج gpt-3.5-turbo بدلاً من gpt-4
        response = openai.ChatCompletion.create (
            model="gpt-3.5-turbo",  # استخدم gpt-3.5-turbo
            messages=[
                {"role": "system", "content": "You are a medical assistant."},
                {"role": "user", "content": f"What is the diagnosis for these symptoms: {symptoms}?"}
            ],
            max_tokens=150  # يمكنك تعديل هذا الرقم بناءً على حجم الاستجابة المطلوبة
        )
        # استخدم التنسيق الصحيح لاستخراج المحتوى من الاستجابة
        return response['choices'][0]['message']['content'].strip ()
    except Exception as e:
        return f"Error: {e}"
