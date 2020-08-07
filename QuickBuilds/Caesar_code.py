def encrypt(text, shift):
    msg = ''
    for ch in text:
        if ch in ['.', ',', '?', '!', '\'', '"', ':', '>', '<']:
            msg += ch
        else:  
            shifted = ord(ch) + shift
            if shifted > 26:
                shifted -= 26
            msg += chr(shifted)
    print("Your txt encrypted is:\n " + msg)

def decrypt(text, shift):
    msg = ''
    for ch in text:
        if ch in ['.', ',', '?', '!', '\'', '"', ':', '>', '<']:
            msg += ch
        else:
            shifted = ord(ch) - shift
            if shifted < 26:
                shifted += 26
            msg += chr(shifted)
    print("Your txt decrypted is:\n " + msg)

while True:
    choice = input(" > (e)ncrypt or (d)ecrypt? ")
    if choice.lower() != "e" and choice.lower() != "d":
        print("\nPlease type in 'e' or 'd' to proceed")
    else:
        try:
            text = input(" > What is your text? ")
            shift = int(input(" > What is your shift?  "))
            assert shift in list(range(26+1))
            if choice.lower() == "e":
                encrypt(text, shift)
                break
            elif choice.lower() == "d":
                decrypt(text, shift)
                break
        except ValueError:
            print('What u typed in \'shift\' is not a number.\nTry again') 
        except AssertionError:
            print('Shift not in range 0-26. \nTry again')
