import sys
def check_passwords(passwords):
    passwords.sort()  # Sorting the passwords to easily identify prefixes

    for i in range(len(passwords) - 1):
        if passwords[i + 1].startswith(passwords[i]):
            return f"BAD PASSWORD"

    return "GOOD PASSWORD"

#Accepting input from the user
input_passwords = input().split()

#Checking the passwords and displaying the output
result = check_passwords(input_passwords)
print(result)
                                                                                                                            