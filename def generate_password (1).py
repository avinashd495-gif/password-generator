def generate_password():
    import random

    # Character pools
    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    nums = ['0','1','2','3','4','5','6','7','8','9']
    syms = ['!', '@', '#', '$', '%', '&', '*']

    # Heello to the reader

    print("PASSWORD CREATOR - Beginner Edition")
    print("Let's make a strong password for you!")

    try:
        num_letters = int(input("How many letters do you want in your password? "))
        num_digits = int(input("How many numbers would you like? "))
        num_symbols = int(input("How many symbols would you prefer? "))
    except:
        print("Please enter a valid number!")
        return

    # Letters can be both upper, lower or both, just ask the user for their preference, simple

    print("Should the letters be 'mixed' case, only 'lower', or only 'upper'? (Enter: mixed/lower/upper)")
    case_type = input().strip().lower()
    password_chars = []

    if case_type == "lower":
        for l in range(num_letters):
            password_chars.append(random.choice(lower))
    elif case_type == "upper":
        for l in range(num_letters):
            password_chars.append(random.choice(upper))
    else:
        # using for, if, elseif and else
        for l in range(num_letters):
            if random.randint(0, 1) == 0:
                password_chars.append(random.choice(lower))
            else:
                password_chars.append(random.choice(upper))

    for n in range(num_digits):
        password_chars.append(random.choice(nums))

    x = 0  # new variable for variety
    while x < num_symbols:
        symbol_pick = random.choice(syms)
        password_chars.append(symbol_pick)
        x = x + 1

    # User can choose to shuffle or not
    wanna_shuffle = input("Do you want the password to be mixed up? (yes/no) ").strip().lower()
    if wanna_shuffle == "yes":
        random.shuffle(password_chars)
    else:
        pass  # Password remains in entered order

    # Manual string building
    password_final = ""
    for item in password
