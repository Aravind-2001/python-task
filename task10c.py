import re
def text_match(text):
    patters = '\w+\s*$'
    if re.search(patters,text):
        return 'found match'
    else:
        return('not found')
print(text_match("
