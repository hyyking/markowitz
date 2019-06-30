import re

def clean_file(content):
    no_comments = re.sub("#.*?\n", "", content)
    no_escape = re.sub("[\n\t\s]", "", no_comments)
    return no_escape
