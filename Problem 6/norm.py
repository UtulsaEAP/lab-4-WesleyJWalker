"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Wesley Walker
Lab Time: Thursday @ 2PM
"""

def norm():
    numlist = list()
    for i in range(0, int(input())):
        numlist.append(float(input()))
    largest_index = 0
    for j in range(0, len(numlist)):
        if numlist[j] > numlist[largest_index]:
            largest_index = j
    for k in range(0, len(numlist)):
        newval = numlist[k] / numlist[largest_index]
        print(f'{newval:.2f}')

if __name__ == "__main__":
    norm()