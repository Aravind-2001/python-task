import re
def text_match(text):
    patters='\w*ab.\w*'
    if re.search(patters,text):
        return ' found match'
    else:
        return('not found')
print(text_match("east or west home is the best"))
print(text_match("abcdefghijklm"))
