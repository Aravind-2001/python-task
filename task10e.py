import re
def text_match(text):
    patterns = '^[a-zA-z_]*$'
    if re.search(patterns, text):
        return 'match found'
    else:
        return("not found")
print(text_match("where there is a well there is a way"))
print(text_match("god create the world beautifully"))
        
