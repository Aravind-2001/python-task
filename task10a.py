import re
def allowed_specified_char(string):
    charre = re.compile(r'[^A-za-z0-9.]')
    string = charre.search(string)
    return not bool(string)
print(allowed_specified_char("ABCDEabcde12345"))
print(allowed_specified_char("!@#$%&"))
