import secrets, string, sys

def get_int(prompt, minimum, maximum=None):
    while True:
        try:
            v = int(input(prompt).strip())
            if v < minimum or (maximum is not None and v > maximum):
                raise ValueError
            return v
        except ValueError:
            rng = f">= {minimum}" if maximum is None else f"{minimum}–{maximum}"
            print(f"Please enter an integer {rng}.")

def choose_charset(level):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"
    if level == 1:
        return lower + digits
    if level == 2:
        return lower + upper + digits
    return lower + upper + digits + symbols

def generate_password(length, charset):
    return ''.join(secrets.choice(charset) for _ in range(length))

def main():
    print("Password Generator")
    length = get_int("Enter desired password length (min 4): ", 4, 1024)
    print("Complexity levels:\n1) Low  (lowercase + digits)\n2) Medium (lower + upper + digits)\n3) High (lower + upper + digits + symbols)")
    level = get_int("Choose complexity level (1-3): ", 1, 3)
    count = get_int("How many passwords to generate (1-20): ", 1, 20)
    charset = choose_charset(level)
    for i in range(count):
        pwd = generate_password(length, charset)
        print(pwd)
    try:
        import pyperclip
        pyperclip.copy(pwd)
        print("\nLast generated password copied to clipboard.")
    except Exception:
        pass

if __name__ == "__main__":
    main()