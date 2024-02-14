"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name: Wesley Walker
Lab Time: Thursday @ 2PM
"""

def brute_eq():
    #Read in first equation, ax + by = c 
    a = int(input())
    b = int(input())
    c = int(input())

    #Read in second equation, dx + ey = f
    d = int(input())
    e = int(input())
    f = int(input())

    solution = False
    for i in range(-10, 10):
        for j in range (-10, 10):
            if (a * i) + (b * j) == c:
                if (d * i) + (e * j) == f:
                    print("x = " + str(i) + " , y = " + str(j))
                    return()
    print("There is no solution")
    
if __name__ == "__main__":
    brute_eq()