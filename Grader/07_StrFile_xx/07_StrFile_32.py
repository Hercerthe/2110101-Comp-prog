def no_lowercase(t):
    if t.upper() == t :
        return True
    return False
def no_uppercase(t):
    if t.lower() == t :
        return True
    return False
def no_number(t):
    for i in t :
        if i in "1234567890" :
            return False
    return True
def no_symbol(t):
    for i in t :
        if i in "~`!!@#$%^&*()_+-=}{][|\\:;\"'<>?,./" :
            return False
    return True
def character_repetition(t):
    for i in range(len(t)-3) :
        if t[i] == t[i+1] == t[i+2] == t[i+3] :
            return True
    return False
def number_sequence(t):
    for i in range(len(t)-3) :
        if (t[i:i+4] in "01234567890") or (t[i:i+4] in "09876543210") :
            return True
    return False
def letter_sequence(t):
    t = t.upper()
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(t)-3) :
        if (t[i:i+4] in letter) or (t[i:i+4] in "".join(sorted(letter,reverse=True))) :
            return True
    return False
def keyboard_pattern(t):
    t = t.upper()
    pattern = "!@#$%^&*()_+ QWERTYUIOP ASDFGHJKL ZXCVBNM"
    for i in range(len(t)-3) :
        if t[i:i+4] in pattern :
            return True
    t = "0" + t
    for i in range(len(t), 3, -1) :
        if t[i:i-4:-1] in pattern :
            return True
    return False
#-----------------------------
passw = input().strip()
errors = []
if len(passw) < 8:
    errors.append("Less than 8 characters")
if no_lowercase(passw):
    errors.append("No lowercase letters")
if no_uppercase(passw):
    errors.append("No uppercase letters")
if no_number(passw):
    errors.append("No numbers")
if no_symbol(passw):
    errors.append("No symbols")
if character_repetition(passw) :
    errors.append("Character repetition")
if number_sequence(passw) :
    errors.append("Number sequence")
if letter_sequence(passw) :
    errors.append("Letter sequence")
if keyboard_pattern(passw) :
    errors.append("Keyboard pattern")
if len(errors) == 0:
    print("OK")
else:
    for i in errors :
        print(i)