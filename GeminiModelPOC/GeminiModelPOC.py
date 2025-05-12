import os
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

import google.generativeai as genai
genai.configure(api_key='AIzaSyAXckQYbEPi8NhDk2bXpUawf3qfMX-nP-c')
model = genai.GenerativeModel('gemini-2.0-flash')

response = model.generate_content("how to file a legal case in consumer court")
print(response.text)

