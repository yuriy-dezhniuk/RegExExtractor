import pyperclip

from reg_ex.phone_numbers_regex import phone_regex
from reg_ex.emails_regex import email_regex


text = str(pyperclip.paste())
matches = []

for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])

print(matches)

