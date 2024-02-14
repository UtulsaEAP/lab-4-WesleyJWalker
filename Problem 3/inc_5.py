"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Wesley Walker
Lab Time: Thursday @ 2PM
"""

def inc_5():
    first = int(input())
    second = int(input())
    sequence = ""
    if second < first:
        print("Second integer can't be less than the first")
        return()
    while first <= second:
        sequence += str(first) + " "
        first += 5
    print(sequence)


if __name__ == '__main__':
    inc_5()