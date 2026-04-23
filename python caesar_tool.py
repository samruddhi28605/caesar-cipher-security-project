import string

# ===== COLORS =====
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


# ===== CORE FUNCTION =====
def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


# ===== SAFE INPUT =====
def get_shift():
    while True:
        try:
            return int(input("Enter shift: "))
        except ValueError:
            print(RED + "❌ Shift must be a number!" + RESET)


# ===== FEATURES =====
def encrypt():
    text = input("Enter text: ")
    shift = get_shift()
    print(GREEN + "Encrypted:", caesar_cipher(text, shift) + RESET)


def decrypt():
    text = input("Enter text: ")
    shift = get_shift()
    print(GREEN + "Decrypted:", caesar_cipher(text, -shift) + RESET)


def brute_force():
    text = input("Enter encrypted text: ")
    print(YELLOW + "\nTrying all shifts:\n" + RESET)
    
    for shift in range(1, 26):
        print(f"{CYAN}Shift {shift}:{RESET} {caesar_cipher(text, -shift)}")


# 🔥 SMART ATTACK (no shift needed)
def smart_attack():
    text = input("Enter encrypted text: ")
    print(YELLOW + "\nTop Possible Decryptions:\n" + RESET)

    for shift in range(1, 6):  # top guesses
        print(f"{CYAN}Guess {shift}:{RESET} {caesar_cipher(text, -shift)}")


def file_encrypt():
    filename = input("Enter file name: ")
    shift = get_shift()
    
    try:
        with open(filename, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(RED + "❌ File not found!" + RESET)
        return
    
    encrypted = caesar_cipher(content, shift)
    
    with open("encrypted.txt", "w") as f:
        f.write(encrypted)
    
    print(GREEN + "File encrypted -> encrypted.txt" + RESET)


# ===== MENU =====
def main():
    while True:
        print(CYAN + "\n===== CAESAR CIPHER TOOL =====" + RESET)
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute Force Attack")
        print("4. Smart Attack (No Shift)")
        print("5. Encrypt File")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            encrypt()
        elif choice == "2":
            decrypt()
        elif choice == "3":
            brute_force()
        elif choice == "4":
            smart_attack()
        elif choice == "5":
            file_encrypt()
        elif choice == "6":
            print(GREEN + "Exiting..." + RESET)
            break
        else:
            print(RED + "Invalid choice!" + RESET)


# ===== ENTRY =====
if __name__ == "__main__":
    main()