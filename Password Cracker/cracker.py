print("=== Password Cracker ===\n")

target_password = input("Enter the target password: ")

password_file = "passwords.txt"

try:
    with open(password_file, 'r', encoding='utf-8') as f:
        for linea in f:
            if linea.strip() == target_password:
                print(f"\n Password found: {target_password}")
                break
        else:
            print("\n Password not found.")
except FileNotFoundError:
    print(f"\n[!] The file '{password_file}' was not found.")
