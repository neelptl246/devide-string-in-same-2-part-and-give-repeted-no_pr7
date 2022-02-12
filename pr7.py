import collections;
testCases = int(input())  # number of test cases
while testCases:        # iterate over the number of test cases
    testCases -= 1
    string = input()        # get the string
    halve = len(string) // 2   
    if len(string) % 2 == 0:      # if the length of the string is even
        if sorted(string[:halve]) == sorted(string[halve:]):  # if the first half is equal to the second half
            print('YES')
        else:                               
    else:                            # if the length is odd
        if sorted(string[:halve]) == sorted(string[halve + 1:]):   
            print('YES')
        else:
            print('NO')
