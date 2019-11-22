new = ""

while True:
    e_o_d = input(" > (e)ncrypt or (d)ecrypt? ")
    if e_o_d.lower() != "e" and e_o_d.lower() != "d":
        print("\nYou were supposed to type in 'e' or 'd'\nPlease try again.\n")
    else:
        intake = input(" > What is it you wanna encrypt? ")
        shift = input(" > What is your shift ")
        if e_o_d.lower() == "e":
            for ch in intake:
                shifted = ord(ch) + int(shift)
                new += chr(shifted)
            print("Your txt encrypted is " + new)
            break
        elif e_o_d.lower() == "d":
            for ch in intake:
                shifted = ord(ch) - int(shift)
                new += chr(shifted)
            print("Your txt decrypted is " + new)
            break

