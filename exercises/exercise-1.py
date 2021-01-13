# 27/10/2020 exercise 1

# helper
def end_exercise():
    print('\n', '-' * 100, '\n')


# example 1
def hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5


def triangle_area(a, b):
    """ Calculates the area of a right triangle.

    Input:
    1) a - First adjacent
    2) b - Second adjacent

    Output (float): Returns the area of the triangle
    """
    return (a * b) / 2


def circumference(a, b, c):
    return a + b + c


print('hypotenuse - ' + str(hypotenuse(3, 4)))
print('triangleArea - ' + str(triangle_area(3, 4)))
print('circumference - ' + str(circumference(3, 4, 5)))
end_exercise()


# example 2
def upper_middle(word):
    middle = len(word) // 2
    word = word.lower()
    return word[:middle] + str.upper(word[middle]) + word[middle + 1:]


print('result of middle upper - ' + upper_middle('wikipedia'))
end_exercise()


# example 3
def count_donuts(donuts):
    if donuts > 10:
        print('Number of donuts: A lot!')
    elif donuts > 5:
        print('Number of donuts:', str(donuts) + '...')
    else:
        print('Number of donuts:', str(donuts) + '.')


count_donuts(11)
end_exercise()
