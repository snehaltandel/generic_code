'''
Write a program that accepts a comma separated sequence of words
as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

def words(a):
    a = str(a).lower().split(',')
    a.sort()
    return a

def entry():
    print('Enter Words Seperated by comma to Sort: ')
    word_input = input()
    return word_input

def word_sort():
    value = entry()
    result = words(value)
    print(result)

word_sort()