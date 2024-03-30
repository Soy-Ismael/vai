import re

def validar_email(email):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return True if re.search(pattern, email) else False


def validar_link(web_site):
    pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return True if re.search(pattern, web_site) else False

# print(validar_email('example@example.com'))
# print(validar_link('https://proyectodalto.com'))