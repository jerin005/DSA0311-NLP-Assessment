import re

text = "My phone number is 9876543210 and email is abc@gmail.com"

phone = re.search(r"\b\d{10}\b", text)
email = re.search(r"\S+@\S+\.\S+", text)

if phone:
    print("Phone Number:", phone.group())
else:
    print("Phone number not found")

if email:
    print("Email:", email.group())
else:
    print("Email not found")

print("All numbers:", re.findall(r"\d+", text))
