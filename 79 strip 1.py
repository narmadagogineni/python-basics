def replace_and_strip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()


txt = "      Nammu is a good girl.....      "
new = replace_and_strip(txt, "Nammu")
print(new)