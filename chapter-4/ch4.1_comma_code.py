'''
Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument
and returns a string with all the items separated by a comma and a space, with and inserted before the last item.
For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.
Be sure to test the case where an empty list [] is passed to your function.
'''

spam = ['apples', 'bananas', 'tofu', 'cats']
cake = [1, 2, 3, 4, 5, 6]
tort = ['Cake', 'Beef', 'Pickled onions', 1 + 2, 5 * 'cake']
empty = []

def comma_code(list):
    try:
        commalist = ''
        for i in list[0:-1]:
            commalist += str(i) + ', '
        commalist = commalist + 'and ' + str(list[-1]) + '. '
        print(commalist[0].upper() + commalist[1:].lower())

    except IndexError:
        print('List must not be empty.')

comma_code(spam)

comma_code(cake)

comma_code(tort)

comma_code(empty)
