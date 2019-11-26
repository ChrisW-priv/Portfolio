try:
    us_name = "ABC"
    user_pass = "123"

    while True:
        make_break = False

        first_in = input("""
     > Would you like to log in og register?
    (log) for logging in
    (reg) for registering
    """)

        while first_in.lower() == "log":
            user_name = input(" > Please insert your username ")
            password = input(" > Please insert your password ")
            if user_name == us_name and password == user_pass:
                print("You have successfully logged in")
                make_break = True
                break
            elif user_name != us_name or password != user_pass:
                print("Either your username or password does not fit")

        while first_in.lower() == "reg":
            new_user = input(" > What would you like to be called from now on? ")
            new_password = input("Set your password ")
            new_password2 = input("Please repeat password ")
            if new_password == new_password2 and 7 < len(new_password) < 24:
                print(f"All looks good. Hi {new_user} it's good to see you.")
                make_break = True
                break
            elif not 7 < len(new_password) < 24:
                print("your password must be 7 characters and can't be longer than 24")
            elif new_password != new_password2:
                print("""
        Passwords are not the same. 
        Press 'a' to try again. 
        If you want to exit just press 'Enter'""")
                try_again = input()
                if try_again.lower() == "a":
                    print("")
                else:
                    print("good bye")
                    break

        if first_in != "reg" and first_in != "log":
            print("""
            Please type in only 'log' or 'reg'""")

        if make_break:
            break
except ValueError:
    print("CoNgRaTuLaTiOnS YoU HaVe SuCcEsFuLly BrOkE My CoDe")
