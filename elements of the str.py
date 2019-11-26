txt = input(" > ")
just_nums = ""
rest = ""

for ch in txt:
    if ord("0") <= ord(ch) <= ord("9"):
        just_nums += ch
    elif not ord("0") <= ord(ch) <= ord("9"):
        rest += ch

print("Nums: " + just_nums)
print("Rest: " + rest)
