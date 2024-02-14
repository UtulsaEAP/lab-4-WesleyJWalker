"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Wesley Walker
Lab Time: Thursday @ 2PM
"""

def password_mod():
    word = input()
    password = ''
    for i in word:
        if i == "i":
            password += "1"
        elif i == "a":
            password += "@"
        elif i == "m":
            password += "M"
        elif i == "B":
            password += "8"
        elif i == "s":
            password += "$"
        else:
            password += str(i)
    password += "!"
    print(password)

if __name__ == "__main__":
    password_mod()