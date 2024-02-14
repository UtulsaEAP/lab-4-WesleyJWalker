"""
Complete the following python code to reverse the string entered by the user.

Name: Wesley Walker
Lab Time: Thursday @ 2PM
"""

def reverse_string():
    done = False
    toPrint = ""
    first = True
    while done == False:
        user_input = str(input())
        if user_input == "Done" or user_input == "done" or user_input == "d":
            done = True
        else:
            if first == False:
                toPrint += "\n"
            first = False
            for i in reversed(range(0, len(user_input))):
                toPrint += user_input[i]
    print(toPrint)
    

if __name__ == "__main__":
    reverse_string()