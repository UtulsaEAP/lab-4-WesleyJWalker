"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Wesley Walker
Lab Time: Thursday @ 2PM

"""


def reverse_binary():
    user_num = int(input())
    toPrint = ""
    while user_num > 0:
        toPrint += str(user_num % 2)
        user_num = user_num // 2
    print(toPrint)

if __name__ == "__main__":
    reverse_binary()